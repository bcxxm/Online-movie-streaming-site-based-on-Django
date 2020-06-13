import polltest.models
from django.shortcuts import render
from polltest.modellist import classList
import re
from django.db.models import Q


def search(request, t):
    context = []
    model_list = []
    # is_have = True
    # if request.method == "POST":
    text = t
    informations = []
    # ispaginator = True
    con = classList
    if text:
        for c in con:
            obj = getattr(polltest.models, c)
            # if re.match(r'^M\w+$', c):
            information = obj.objects.filter(Q(language__contains=text)
                                             | Q(tv_name__contains=text)
                                             | Q(star__contains=text)
                                             | Q(tv_type__contains=text)
                                             | Q(director__contains=text))
            if len(information):
                model_list.append(c)
                # for foo in information:
                context.append(information)
                # for foo in information:
                #     informations.append(foo)
        # print(informations)
        # conte = paginator(request, informations, 20)
        # if len(context):
        #     is_have = False
        cont = {'con': context, 'model_list': model_list,}
        return render(request, 'polltest/search.html', cont)


def search_play_context(request, tab, n):
    table = getattr(polltest.models, tab)
    n = int(n)
    con = table.objects.filter(Q(id__gte=str(n)) & Q(id__lte=str(n + 19)))
    if re.match(r'^M', tab):
        tap = True
        if len(re.split(r',', con[0].star)) > 4:
            star_name = re.split(r',', con[0].star)[0:4]
        else:
            star_name = re.split(r',', con[0].star)
        # con = table.objects.filter(Q(id__gte=str(n)) & Q(id__lte=str(n + 19)))
        context = {'context': con, 'starNames': star_name, 'type': tab, 'num': n, 'tap': tap}
    else:
        tap = False
        text = tab+'Noe'
        table1 = getattr(polltest.models, text)
        con = table.objects.filter(Q(id__gte=str(n)) & Q(id__lte=str(n + 19)))
        cont = table1.objects.filter(tv_id=n)
        if len(re.split(r'[,/]', con[0].star)) > 4:
            star_name = re.split(r'[,/]', con[0].star)[0:4]
        else:
            star_name = re.split(r'[,/]', con[0].star)
        context = {'context': con, 'cont': cont, 'starNames': star_name, 'type': tab, 'num': n, 'tap': tap}
    return render(request, 'polltest/playContent.html', context)


def search_play(request, tab, n):
    table = getattr(polltest.models, tab)
    text = request.GET.get('value')
    n1 = re.split(r'-', text)
    n2 = int(n)
    con = table.objects.filter(Q(id__gte=n2) & Q(id__lte=str(n2 + 8)))
    if re.match(r'^M', tab):
        if int(n1[1]) == 1:
            m_url = con[0].mv_url
        else:
            m_url = con[0].mu_url
        context = {'context': con, 'big': None, 'type': tab, 'num': n, 'm_url': m_url}
        return render(request, 'polltest/play.html', context)
    elif re.match(r'^V', tab):
        text = tab + 'Noe'
        table1 = getattr(polltest.models, text)
        cont = table1.objects.filter(tv_id=n)
        if int(n1[1]) == 1:
            m_url = cont[int(n1[2])-1].tv_url
        else:
            m_url = cont[int(n1[2])-1].tu_url
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
                context = {'context': con, 'big': None, 'type': tab, 'num': n, 'm_url': m_url}
                return render(request, 'polltest/play.html', context)


