# coding=utf-8
import datetime
from django.db import models
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

    def __str__(self):
        return self.patient.name + ' ' + self.patient.last_name + ' - ' + \
               str(self.height)


@python_2_unicode_compatible
class PatientVisit(models.Model):
    date = models.DateField(verbose_name='Fecha de Visita',
                            default=datetime.date.today())
    description = models.TextField(verbose_name='Detalles de la Consulta',
                                   blank=True, null=True)
    patient_stats = models.ForeignKey(PatientStat,
                                      verbose_name='Valores del Paciente')

    def __str__(self):
        return str(self.date) + ' ' + self.patient_stats.patient.name + ' ' + \
               self.patient_stats.patient.last_name
