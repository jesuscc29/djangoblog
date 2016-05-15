# coding=utf-8
import datetime
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView
from office.forms import AddPatientForm, PatientStatsForm, PatientVisitForm, \
    PersonForm, PersonPaymentForm
from office.functions import LoginRequiredMixin, get_patient_stat_list, \
    get_patient_weight_stats
from office.models import Patient, PatientVisit, PatientStat, Person, \
    PersonPayment
from recipes import response_json


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
                patient__pk=patient['pk']).last()
            patient.update(last_visit=last_visit)
            patient.update(age=age)
            patient.update(progress=get_patient_weight_stats(patient['pk']))
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
    pk = None

    def get_object(self, queryset=None):
        self.pk = self.kwargs.get('pk', None)
        if self.pk is not None:
            patient = Patient.objects.get(pk=self.pk)
            return patient
        else:
            raise AttributeError('No pk found')

    def get_context_data(self, **kwargs):
        context = super(PatientDetail, self).get_context_data(**kwargs)
        stats = get_patient_stat_list(self.pk)
        visits = PatientVisit.objects.filter(
            patient__pk=self.pk).order_by('date')
        context['patient_stats'] = stats
        context['patient_visits'] = visits
        context['visit_form'] = PatientVisitForm()
        context['stats'] = get_patient_weight_stats(self.pk)
        context['form'] = PatientStatsForm()
        return context


def save_patient_stats(request, pk):
    if pk is not None:
        form = PatientStatsForm(request.POST or None)
        patient = Patient.objects.get(pk=pk)
        if form.is_valid():
            stats = form.save(commit=False)
            stats.patient = patient
            stats.save()
            return response_json("OK", 200)
        else:
            error = dict()
            error['message'] = 'El formulario no es válido.'
            return response_json(error, 400)
        pass
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


def edit_patient_stats(request, pk):
    if pk is not None:
        curr_stats = PatientStat.objects.get(pk=pk)
        form = PatientStatsForm(request.POST or None,
                                instance=curr_stats)
        if form.is_valid():
            stats = form.save(commit=False)
            stats.save()
            return response_json("OK", 200)
        else:
            error = dict()
            error['message'] = 'El formulario no es válido.'
            return response_json(error, 400)
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


def remove_patient_status(request, pk):
    if pk is not None:
        stats = PatientStat.objects.get(pk=pk)
        stats.delete()
        return response_json("OK", 200)
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


def get_patient_stats(request, pk):
    if pk is not None:
        stats = PatientStat.objects.filter(pk=pk).values(
            'height', 'weight', 'activity', 'stats_date'
        )
        # stats['stats_date'] = stats['stats_date'].strftime("%Y-%m-%d")
        for stat in stats:
            stat.update(date_str=stat['stats_date'].strftime('%Y-%m-%d'))
        return response_json(list(stats), 200)
    else:
        error = dict()
        error['message'] = 'Pk not send.'
        return response_json(error, 404)


def save_patient_visit(request, pk):
    if pk is not None:
        form = PatientVisitForm(request.POST or None)
        patient = Patient.objects.get(pk=pk)
        if form.is_valid():
            visit_obj = form.save(commit=False)
            visit_obj.patient = patient
            visit_obj.save()
            return response_json("OK", 200)
        else:
            error = dict()
            error['message'] = 'El formulario no es válido.'
            return response_json(error, 400)
        pass
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


def edit_patient_visit(request, pk):
    if pk is not None:
        curr_visit = PatientVisit.objects.get(pk=pk)
        form = PatientVisitForm(request.POST or None,
                                instance=curr_visit)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.save()
            return response_json("OK", 200)
        else:
            print form.errors
            error = dict()
            error['message'] = 'El formulario no es válido.'
            return response_json(error, 400)
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


def get_patient_visit_details(request, pk):
    if pk is not None:
        visits = PatientVisit.objects.filter(pk=pk).values(
            'date', 'description'
        )
        # stats['stats_date'] = stats['stats_date'].strftime("%Y-%m-%d")
        for visit in visits:
            visit.update(date_str=visit['date'].strftime('%Y-%m-%d'))
        return response_json(list(visits), 200)
    else:
        error = dict()
        error['message'] = 'Pk not send.'
        return response_json(error, 404)


def remove_patient_visit(request, pk):
    if pk is not None:
        visit = PatientVisit.objects.get(pk=pk)
        visit.delete()
        return response_json("OK", 200)
    else:
        error = dict()
        error['message'] = 'Object PK not sent.'
        return response_json(error, 404)


# ======== Views Containing Money COunt Functions
class PersonList(ListView):
    template_name = 'money/person_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        persons = Person.objects.all()
        return persons

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['person_form'] = PersonForm()
        context['person_payment_form'] = PersonPaymentForm()
        return context


def person_add(request):
    person_form = PersonForm(request.POST or None)
    if person_form.is_valid:
        person = person_form.save(commit=False)
        person.save()
        return response_json('OK', 200)
    else:
        return response_json('Error guardando a la persona', 500)


def person_payment_add(request):
    person_payment_form = PersonPaymentForm(request.POST or None)
    if person_payment_form.is_valid:
        payment = person_payment_form.save(commit=False)
        payment.save()
        return response_json("OK", 200)
    else:
        return response_json('Error guardando el pago de la persona', 500)


def get_person_payments(request, pk):
    if pk is not None:
        payments = PersonPayment.objects.filter(person__pk=pk).values(
            'payment_date', 'amount_payed').order_by('-payment_date')
        payment_list = list()
        for payment in payments:
            new_payment = dict()
            new_payment['payment_date'] = payment['payment_date'].strftime('%d %b %Y')
            new_payment['amount_payed'] = payment['amount_payed']
            payment_list.append(new_payment)
        return response_json(payment_list, 200)
    else:
        return response_json('No se envio un ID de persona', 404)


def remove_person(request, pk):
    if pk is not None:
        person_payments = PersonPayment.objects.filter(person__pk=pk)
        person_payments.delete()
        person = Person.objects.get(pk=pk)
        person.delete()
        return response_json("OK", 200)
    else:
        return response_json("Error eliminando la persona seleccionada", 500)