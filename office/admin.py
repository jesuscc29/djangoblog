from django.contrib import admin
from office.models import PatientVisit, PatientStat, Patient

admin.site.register(Patient)
admin.site.register(PatientStat)
admin.site.register(PatientVisit)