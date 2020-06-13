import polltest.models
from django.shortcuts import render
from django.db.models import Q
import re


def play_context(request, big, tab, n):
    table = getattr(polltest.models, tab)
    n = int(n)
    if re.match(r'^M', tab):
        tap = True
        con = table.objects.filter(Q(id__gte=str(n)) & Q(id__lte=str(n + 19)))
        if len(re.split(r'[,/]', con[0].star)) > 4:
            star_name = re.split(r'[,/]', con[0].star)[0:4]
        else:
            star_name = re.split(r'[,/]', con[0].star)
        context = {'context': con, 'big': big, 'starNames': star_name, 'type': tab, 'num': n, 'tap': tap}
    else:
        tap = False
        text = tab + 'Noe'
        table1 = getattr(polltest.models, text)
        con = table.objects.filter(Q(id__gte=str(n)) & Q(id__lte=str(n + 19)))
        cont = table1.objects.filter(tv_id=n)
        if len(re.split(r',', con[0].star)) > 4:
            star_name = re.split(r',', con[0].star)[0:4]
        else:
            star_name = re.split(r',', con[0].star)
        context = {'context': con, 'cont': cont, 'starNames': star_name, 'big': big,  'type': tab, 'num': n, 'tap': tap}
    return render(request, 'polltest/playContent.html', context)


def play(request, big, tab, n):
    table = getattr(polltest.models, tab)
    text = request.GET.get('value')
    n1 = re.split(r'-', text)
    n2 = int(n)
    # n3 = int(n1[1])
    con = table.objects.filter(Q(id__gte=n2) & Q(id__lte=str(n2 + 8)))
    if re.match(r'^M', tab):
        if int(n1[1]) == 1:
            m_url = con[0].mv_url
        else:
            m_url = con[0].mu_url
        context = {'context': con, 'big': None, 'type': tab, 'num': n, 'm_url': m_url}
        return render(request, 'polltest/play.html', context)
    else:
        text = tab + 'Noe'
        table1 = getattr(polltest.models, text)
        cont = table1.objects.filter(tv_id=n)
        for foo in cont:
            if re.split(r'(\d+)', foo.one_set)[1] == str(n1[2]):
                if int(n1[1]) == 1:
                    m_url = foo.tv_url
                else:
                    m_url = foo.tu_url
                context = {'context': con, 'big': big, 'type': tab, 'num': n, 'm_url': m_url}
                return render(request, 'polltest/play.html', context)
