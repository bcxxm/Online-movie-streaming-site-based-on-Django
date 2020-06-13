from django.shortcuts import render
from polltest.paginator import paginator
from polltest.models import *
# from django.contrib.contenttypes.models import ContentType
# from django import forms
import polltest.models
from django.db.models import Q
from polltest.modellist import class_dict, get_content, get_pf
from polltest.search import search, search_play, search_play_context
from polltest.play import play, play_context
import random
# import heapq


# 首页
def index(request):
    context = get_content('A')
    return render(request, 'polltest/index.html', context)


# 二维码
def quickmark(request):
    return render(request, 'polltest/quickmark.html')


# 热门影片
def hot(request):
    context = get_content('H')
    # context = paginator(request, con, 25)
    return render(request, 'polltest/hot.html', context)


# 电视剧
def teleplay(request):
    context = get_content('T')
    rankings = get_pf('T')
    context['rankhot'] = rankings[0]
    context['ranknew'] = rankings[1]
    context['ranksearch'] = rankings[2]
    return render(request, 'polltest/teleplay.html', context)


def teleplay_type(request, tab):
    table = getattr(polltest.models, tab)
    con = table.objects.all().order_by('-id')
    rankings = table.objects.filter(pf=10)
    if len(rankings) > 15:
        ranking = random.sample(list(rankings), 15)
    else:
        rankings = table.objects.filter(Q(pf__gt=8))
        ranking = random.sample(list(rankings), 15)
    context = paginator(request, con, 25)
    context.update(big_type='电视剧', verbose_name=class_dict[tab])
    context['rank'] = ranking
    return render(request, 'polltest/all_type.html', context)


# 电影
def movie(request):
    context = get_content('M')
    rankings = get_pf('M')
    context['rankhot'] = rankings[0]
    context['ranknew'] = rankings[1]
    context['ranksearch'] = rankings[2]
    return render(request, 'polltest/movie.html', context)


def movie_type(request, tab):
    table = getattr(polltest.models, tab)
    con = table.objects.all().order_by('-id')
    rankings = table.objects.filter(pf=10)
    if len(rankings) > 15:
        ranking = random.sample(list(rankings), 15)
    else:
        rankings = table.objects.filter(Q(pf__gt=8))
        ranking = random.sample(list(rankings), 15)
    context = paginator(request, con, 25)
    context.update(big_type='电影', verbose_name=class_dict[tab])
    context['rank'] = ranking
    return render(request, 'polltest/all_type.html', context)


# 动漫
def comic(request):
    context = get_content('C')
    rankings = get_pf('C')
    context['rankhot'] = rankings[0]
    context['ranknew'] = rankings[1]
    return render(request, 'polltest/comic.html', context)


def comic_type(request, tab):
    table = getattr(polltest.models, tab)
    con = table.objects.all().order_by('-id')
    rankings = table.objects.filter(pf=10)
    if len(rankings) > 15:
        ranking = random.sample(list(rankings), 15)
    else:
        rankings = table.objects.filter(Q(pf__gt=9))
        ranking = random.sample(list(rankings), 15)
    context = paginator(request, con, 25)
    context.update(big_type='动漫', verbose_name=class_dict[tab])
    context['rank'] = ranking
    return render(request, 'polltest/all_type.html', context)


# 综艺
def variety_show(request):
    con = VarietyShow.objects.all().order_by('-id')
    rankings = VarietyShow.objects.filter(pf=10)
    # ranking = VarietyShow.objects.filter(Q(pf__gte=9.5) & Q(pf__lt=10))
    #     # print(len(ranking))
    if len(rankings) > 15:
        ranking = random.sample(list(rankings), 15)
    else:
        ranking = rankings
    context = paginator(request, con, 25)
    context['rank'] = ranking
    # print(context, len(rankings))
    return render(request, 'polltest/variety.html', context)










