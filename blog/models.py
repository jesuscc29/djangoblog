import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


@python_2_unicode_compatible
class Tag(models.Model):
    tag = models.CharField(max_length=64, verbose_name='Tag')

    def __str__(self):
        return self.tag


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Post Title')
    slug = models.SlugField(max_length=155, editable=False)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.PROTECT)
    published_date = models.DateTimeField(default=datetime.datetime.now())
    last_edited = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name='Content')
    published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    featured_image = models.ImageField(upload_to="blog", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="blog", blank=True, null=True)

    __image_field = None

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.__image_field = self.featured_image

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        if self.__image_field != self.featured_image:
            # La imagen ha cambiado
            from PIL import Image
            import os
            from cStringIO import StringIO
            from django.core.files.uploadedfile import SimpleUploadedFile
            from django.conf import settings

            image = Image.open(
                os.path.join(settings.MEDIA_ROOT, self.featured_image.name)
            )
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')

            h_o = image.size[1]
            w_o = image.size[0]
            w, h = self.scale_dimensions(w_o, h_o, 200)
            image.thumbnail((w, h), Image.ANTIALIAS)

            temp_handle = StringIO()
            image.save(temp_handle, 'png')

            temp_handle.seek(0)
            # save to model
            suf = SimpleUploadedFile(
                os.path.split(self.featured_image.name)[-1],
                temp_handle.read(),
                content_type="image/png"
            )

            self.thumbnail.save(suf.name+'.png', suf, save=False)
            super(Post, self).save()



    @staticmethod
    def scale_dimensions(width, height, longest_side):
        """ Calculates image ratio given a longest side
        returns a tupple with ajusted width, height
        @param width:  integer, the current width of the image
        @param height:  integer, the current height of the image
        @param longest_side:   the longest side of the resized image
        @return: resized width, height
        """
        if width > height:
            if width > longest_side:
                ratio = longest_side*1./width
                return int(width*ratio), int(height*ratio)
        elif height > longest_side:
            ratio = longest_side*1./height
            return int(width*ratio), int(height*ratio)
        return width, height
