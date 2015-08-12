import datetime
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView
from office.forms import AddPatientForm, PatientStatsForm
from office.functions import LoginRequiredMixin
from office.models import Patient, PatientVisit


class PatientList(LoginRequiredMixin, ListView):
    template_name = 'office/patient_list.html'

    def get_queryset(self):
        patients = Patient.objects.all()
        return patients

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super(PatientList, self).get_context_data(**kwargs)
        GENDERS = ['Mujer', 'Hombre']
        patients_pks = Patient.objects.all().values_list('pk', flat=True)
        patients = Patient.objects.all().values(
            'name', 'last_name', 'gender', 'phone_number', 'email',
            'pk', 'birthday'
        )
        for patient in patients:
            age = today - patient['birthday']
            age = age.days / 365
            last_visit = PatientVisit.objects.filter(
                patient_stats__patient__pk=patient['pk']).last()
            patient.update(last_visit=last_visit)
            patient.update(age=age)
        context['patients'] = patients
        return context


class PatientCreate(LoginRequiredMixin, CreateView):
    template_name = 'generic/generic_form.html'
    success_url = reverse_lazy('patient_list')
    model = Patient
    form_class = AddPatientForm

    def get_context_data(self, **kwargs):
        context = super(PatientCreate, self).get_context_data(**kwargs)
        context['subject'] = 'Paciente'
        context['operation'] = 'Alta'
        return context


class PatientDetail(LoginRequiredMixin, DetailView):
    template_name = 'office/patient_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            patient = Patient.objects.get(pk=pk)
            return patient
        else:
            raise AttributeError('No pk found')

    def get_context_data(self, **kwargs):
        context = super(PatientDetail, self).get_context_data(**kwargs)
        context['form'] = PatientStatsForm(instance=self.get_object())
        return context


def save_patient_stats(request, pk):
    if pk is not None:
        pass
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)
