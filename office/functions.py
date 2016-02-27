# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from office.models import PatientStat

__author__ = 'jesuscc29'


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='login')


def get_patient_stat_list(pk):
    activity = PatientStat.ACTIVITY
    stats = PatientStat.objects.filter(
        patient__pk=pk
    ).values(
        'height', 'weight', 'activity', 'stats_date', 'pk'
    ).order_by('stats_date')
    for stat in stats:
        stat.update(activity=activity[int(stat['activity'])][1])
        last = PatientStat.objects.filter(
            stats_date__lt=stat['stats_date']
        ).values('height', 'weight').order_by('-stats_date')
        if len(last):
            if last[0]['weight'] > stat['weight']:
                stat.update(down=True)
                stat.update(down_value=last[0]['weight']-stat['weight'])
            elif last[0]['weight'] < stat['weight']:
                stat.update(up=True)
                stat.update(up_value=stat['weight']-last[0]['weight'])
            stat.update(last_weight=last[0]['weight'])
        else:
            stat.update(last_weight=None)
    return stats


def get_patient_weight_stats(patient_pk):
    data = dict()
    init_stat = PatientStat.objects.filter(
        patient__pk=patient_pk).values('weight', 'stats_date'
    ).order_by('stats_date')
    end_stat = PatientStat.objects.filter(
        patient__pk=patient_pk).values('weight', 'stats_date'
    ).order_by('-stats_date')
    if len(init_stat) > 0 and len(end_stat) > 0:
        init_date = init_stat[0]['stats_date']
        init_weight = init_stat[0]['weight']
        end_weight = end_stat[0]['weight']
        difference = init_weight - end_weight
        data['init_date'] = init_date
        if difference > 0:
            data['weight_down'] = True
            data['weight'] = difference
        else:
            data['weight_down'] = False
            data['weight'] = difference * -1
        return data
    else:
        return None
