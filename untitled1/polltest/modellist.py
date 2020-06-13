from django.db.models import Q, Max
import polltest.models
from polltest.models import *
import re
import random


class_dict = {'MovieHot': '热门影片', 'MovieAction': '动作片', 'MovieComedy': '喜剧片',
              'MovieLove': '爱情片', 'MoviePanic': '恐怖片', 'MovieScience': '科幻片',
              'MovieWar': '战争片', 'MoviePlot': '剧情片', 'TvMLS': '大陆剧', 'TvEA': '欧美剧',
              'TvHKT': '港台剧', 'TvJSK': '日韩剧', 'TvOverSeas': '海外剧',
              'ComicJSK': '日韩动漫', 'ComicML': '国产动漫', 'ComicOther': '欧美动漫',
              }

classList = ['MovieHot', 'MovieAction', 'MovieComedy',
             'MovieLove', 'MoviePanic', 'MovieScience',
             'MovieWar', 'TvMLS', 'TvEA',
             'TvHKT', 'TvJSK', 'TvOverSeas',
             'ComicJSK', 'ComicML', 'ComicOther',
             'VarietyShow'
             ]

movieList = ['MovieHot', 'MovieAction', 'MovieComedy',
             'MovieLove', 'MoviePanic', 'MovieScience',
             'MovieWar']

tvList = ['TvMLS', 'TvEA', 'TvHKT', 'TvJSK', 'TvOverSeas']

comicList = ['ComicJSK', 'ComicML', 'ComicOther']


def get_content(types):
    if types == 'M':
        action = MovieAction.objects.all().order_by('-id')[:10]
        war = MovieWar.objects.all().order_by('-id')[:10]
        comedy = MovieComedy.objects.all().order_by('-id')[:10]
        love = MovieLove.objects.all().order_by('-id')[:10]
        science = MovieScience.objects.all().order_by('-id')[:10]
        panic = MoviePanic.objects.all().order_by('-id')[:10]
        context = {'action': action, 'war': war, 'comedy': comedy,
                   'love': love, 'science': science, 'panic': panic}
    elif types == 'T':
        mls = TvMLS.objects.all().order_by('-id')[:10]
        ea = TvEA.objects.all().order_by('-id')[:10]
        jsk = TvJSK.objects.all().order_by('-id')[:10]
        hsk = TvHKT.objects.all().order_by('-id')[:10]
        overseas = TvOverSeas.objects.all().order_by('-id')[:10]
        context = {'mls': mls, 'ea': ea, 'jsk': jsk, 'hsk': hsk, 'overseas': overseas}
    elif types == 'C':
        ml = ComicML.objects.all().order_by('-id')[:10]
        jsks = ComicJSK.objects.all().order_by('-id')[:10]
        other = ComicOther.objects.all().order_by('-id')[:10]
        context = {'ml': ml, 'jsk': jsks, 'other': other}
    elif types == 'V':
        vs = VarietyShow.objects.all().order_by('-id')[:10]
        context = {'vs': vs}
    elif types == 'H':
        mv_hot = MovieAction.objects.all().order_by('-id')[:10]
        tv_hot = TvMLS.objects.all().order_by('-id')[:10]
        comic_hot = ComicJSK.objects.all().order_by('-id')[:10]
        vs_hot = VarietyShow.objects.filter(pf__gte=9.5)[0:6]
        context = [mv_hot, tv_hot, comic_hot, vs_hot]
        context = {'context': context}
        return context
    else:
        # 电影
        mv_pf = MovieAction.objects.filter(pf=10)[0:15]
        mv_hot = mv_pf[3]
        if len(re.split(r'[,，/]', mv_hot.star)) > 3:
            mhsn = re.split(r'[,，/]', mv_hot.star)[0:3]
        else:
            mhsn = re.split(r'[,，/]', mv_hot.star)
        action = MovieAction.objects.filter(Q(id__gte='50') & Q(id__lte='59')).order_by('id')
        war = MovieWar.objects.filter(id__lte='10')
        comedy = MovieComedy.objects.filter(id__lte='10')
        love = MovieLove.objects.filter(id__lte='10')
        science = MovieScience.objects.filter(id__lte='10')
        panic = MoviePanic.objects.filter(id__lte='10')
        # 电视剧
        tv_pf = TvMLS.objects.filter(pf=10)[0:15]
        tv_hot = tv_pf[0]
        if len(re.split(r'[,/]', tv_hot.star)) > 3:
            thsn = re.split(r'[,/]', tv_hot.star)[0:3]
        else:
            thsn = re.split(r'[,/]', tv_hot.star)
        mls = TvMLS.objects.filter(Q(id__gte='2193') & Q(id__lte='2202')).order_by('id')
        ea = TvEA.objects.filter(id__lte='10')
        jsk = TvJSK.objects.filter(id__lte='10')
        hsk = TvHKT.objects.filter(id__lte='10')
        overseas = TvOverSeas.objects.filter(id__lte='10')
        # 动漫
        # ml = ComicML.objects.filter(id__lte='3')
        comics = ComicJSK.objects.filter(id__lte='10')
        comic_pf = ComicJSK.objects.filter(pf__gte=9)[0:15]
        # other = ComicOther.objects.filter(id__lte='2')
        # 综艺
        vs_pf = VarietyShow.objects.filter(pf__gte=9)[0:15]
        vs_hot = vs_pf[2]
        if len(re.split(r'[,/]', vs_hot.star)) > 3:
            vhsn = re.split(r'[,/]', vs_hot.star)[0:3]
        else:
            vhsn = re.split(r'[,/]', vs_hot.star)
        vs = VarietyShow.objects.filter(id__lte='10')
        # 轮番图
        # lft = [mv_pf[random.randint(0, len(mv_pf)-1)], tv_pf[random.randint(0, len(tv_pf)-1)],
        #        comic_pf[random.randint(0, len(comic_pf)-1)], tv_pf[random.randint(0, len(tv_pf)-1)],
        #        mv_pf[random.randint(0, len(mv_pf)-1)]]
        lft = [MovieAction.objects.all().order_by('-id')[0],  TvMLS.objects.all().order_by('-id')[0],
               ComicJSK.objects.all().order_by('-id')[0], TvMLS.objects.all().order_by('-id')[1],
               MovieAction.objects.all().order_by('-id')[1]
               ]
        context = {'mv_hot': mv_hot, 'mhsn': mhsn, 'action': action, 'war': war, 'comedy': comedy,
                   'love': love, 'science': science, 'panic': panic, 'tv_hot': tv_hot, 'thsn': thsn,
                   'mls': mls, 'ea': ea, 'jsk': jsk, 'hsk': hsk, 'overseas': overseas,
                   'comics': comics, 'vs': vs, 'vs_hot': vs_hot, 'vhsn': vhsn, 'lft': lft,
                   'mv_pf': mv_pf, 'tv_pf': tv_pf, 'comic_pf': comic_pf, 'vs_pf': vs_pf,
                   }
    return context


def get_pf(types):
    ranks = []
    if types == 'M':
        for movie in movieList:
            table = getattr(polltest.models, movie)
            rank = table.objects.filter(pf__gte=9.5)
            for pfs in rank:
                ranks.append(pfs)
        rankinghot = random.sample(ranks, 15)
        rankingnew = random.sample(ranks, 15)
        rankingsearch = random.sample(ranks, 15)
        context = [rankinghot, rankingnew, rankingsearch]
    elif types == 'T':
        for tv in tvList:
            table = getattr(polltest.models, tv)
            rank = table.objects.filter(pf__gte=9.5)
            for pfs in rank:
                ranks.append(pfs)
        rankinghot = random.sample(ranks, 15)
        rankingnew = random.sample(ranks, 15)
        rankingsearch = random.sample(ranks, 15)
        context = [rankinghot, rankingnew, rankingsearch]
    if types == 'C':
        for comic in comicList:
            table = getattr(polltest.models, comic)
            rank = table.objects.filter(pf__gte=9.5)
            for pfs in rank:
                ranks.append(pfs)
        rankinghot = random.sample(ranks, 15)
        rankingnew = random.sample(ranks, 15)
        context = [rankinghot, rankingnew]
    return context



