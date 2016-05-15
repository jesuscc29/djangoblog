# coding=utf-8
import datetime
from django.db import models
from django.db.models import Sum
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Patient(models.Model):
    GENDER = (
        (0, 'Mujer'),
        (1, 'Hombre')
    )
    name = models.CharField(max_length=72, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=72, verbose_name='Apellido(s)')
    gender = models.SmallIntegerField(choices=GENDER, default=0,
                                      verbose_name='Sexo')
    birthday = models.DateField(verbose_name='Fecha de Nacimiento',
                                default=datetime.date.today())
    register_date = models.DateField(verbose_name='Fecha de Registro',
                                     default=datetime.date.today())
    phone_number = models.CharField(max_length=72, verbose_name='Teléfono',
                                    blank=True, null=True)
    email = models.CharField(max_length=125, verbose_name='Correo Electrónico',
                             blank=True, null=True)

    def __str__(self):
        return ' '.join([self.name, self.last_name])


@python_2_unicode_compatible
class PatientStat(models.Model):
    ACTIVITY = (
        (0, 'Ninguna'),
        (1, 'Bajo'),
        (2, 'Moderada'),
        (3, 'Constante'),
        (4, 'Deportista')
    )
    height = models.DecimalField(verbose_name='Altura',
                                 max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    weight = models.DecimalField(verbose_name='Peso',
                                 max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    activity = models.SmallIntegerField(choices=ACTIVITY,
                                        default=2,
                                        verbose_name='Actividad Física')
    patient = models.ForeignKey(Patient, verbose_name='Paciente')
    stats_date = models.DateField(default=datetime.date.today(),
                                  verbose_name='Fecha de datos')

    def __str__(self):
        return self.patient.name + ' ' + self.patient.last_name + ' - ' + \
               str(self.height)


@python_2_unicode_compatible
class PatientVisit(models.Model):
    date = models.DateField(verbose_name='Fecha de Visita',
                            default=datetime.date.today())
    description = models.TextField(verbose_name='Detalles de la Consulta',
                                   blank=True, null=True)
    patient = models.ForeignKey(Patient, verbose_name='Paciente')

    def __str__(self):
        return str(self.date) + ' ' + self.patient.name + ' ' + \
               self.patient.last_name


@python_2_unicode_compatible
class Person(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Nombre')
    num_guest = models.IntegerField(max_length=2,
                                    verbose_name='Num. Invitados',
                                    default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name='Monto Total')
    amount_left = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name='Monto Restante',
                                      blank=True,
                                      null=True)

    def __str__(self):
        return self.full_name + ': $' + str(self.amount_left)

    def save(self, *args, **kwargs):
        if self.amount_left is None:
            self.amount_left = self.total_amount
        super(Person, self).save()


@python_2_unicode_compatible
class PersonPayment(models.Model):
    person = models.ForeignKey(Person, verbose_name='Persona')
    payment_date = models.DateTimeField(verbose_name='Fecha de Pago',
                                        default=datetime.datetime.now())
    amount_payed = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name='Cantidad Pagada')

    def __str__(self):
        return self.person.full_name + ': $' + str(self.amount_payed)

    def save(self, *args, **kwargs):
        if self.person.amount_left is not None:
            self.person.amount_left = self.person.amount_left - self.amount_payed
        else:
            self.person.amount_left = self.amount_payed
        self.person.save()
        super(PersonPayment, self).save()
