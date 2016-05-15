from django.contrib import admin
from office.models import PatientVisit, PatientStat, Patient, Person, \
    PersonPayment

admin.site.register(Patient)
admin.site.register(PatientStat)
admin.site.register(PatientVisit)
admin.site.register(Person)
admin.site.register(PersonPayment)
