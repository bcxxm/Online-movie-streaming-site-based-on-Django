import xadmin
from xadmin.views import CommAdminView, BaseAdminView
from .models import *


class MovieActionAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'

    ordering = ('id',)
    show_detail_fields = ['tv_type']
    # list_order =


class MovieScienceAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'

    ordering = ('id',)
    show_detail_fields = ['tv_type']


class MovieWarAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'

    ordering = ('id',)
    show_detail_fields = ['tv_type']


class MovieLoveAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)
    show_detail_fields = ['tv_type']


class MoviePanicAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)
    show_detail_fields = ['tv_type']


class MovieComedyAdmin(object):
    # data_charts = {"MovieDongzuo"(模型类名): {"title": u"动作电影", "x-field"（X坐标）: "time",
    #                                 "y-field"（Y坐标）: ("name",)"order": ('time',),} }
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "time"]
    # model_icon = 'fa fa-camera-retro'

    ordering = ('id',)
    show_detail_fields = ['tv_type']


# 全局设置
class GlobalSetting(object):
    site_title = '怀哥电影网站管理后台'
    site_footer = '我的网站'
    apps_label_title = {'polltest': u'电影'}
    apps_icons = {'polltest': 'fa fa-camera-retro'}


# 基本设置
class BaseSetting(object):
    # 使能更换主题
    enable_themes = True


class TvMainLandNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvMainLandAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvMainLandNoeAdmin, ]
    ordering = ('id',)


class TvMLSNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvMLSAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvMLSNoeAdmin, ]
    ordering = ('id',)


class TvEANoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvEAAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvEANoeAdmin, ]
    ordering = ('id',)


class TvHKTNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvHKTAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvHKTNoeAdmin, ]
    ordering = ('id',)


class TvJSKNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvJSKAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvJSKNoeAdmin, ]
    ordering = ('id',)


class TvOverSeasNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class TvOverSeasAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [TvOverSeasNoeAdmin, ]
    ordering = ('id',)


class ComicJSKNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class ComicJSKAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [ComicJSKNoeAdmin, ]
    ordering = ('id',)


class ComicMLNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class ComicMLAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [ComicMLNoeAdmin, ]
    ordering = ('id',)


class ComicOtherNoeAdmin(object):
    list_display = ["id", "one_set", ]
    list_per_page = 20
    style = 'tab'
    # list_filter = ["id", "tv_name", "tv_type"]
    # model_icon = 'fa fa-camera-retro'
    ordering = ('id',)


class ComicOtherAdmin(object):
    list_display = ["id", "tv_name", "time"]
    list_per_page = 20
    list_filter = ["id", "tv_name", "tv_type"]
    search_fields = ('id', 'tv_name', 'time')
    # model_icon = 'fa fa-camera-retro'
    inlines = [ComicOtherNoeAdmin, ]
    ordering = ('id',)


xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(MovieAction, MovieActionAdmin)
xadmin.site.register(MovieScience, MovieScienceAdmin)
xadmin.site.register(MovieWar, MovieWarAdmin)
xadmin.site.register(MovieLove, MovieLoveAdmin)
xadmin.site.register(MovieComedy, MovieComedyAdmin)
xadmin.site.register(MoviePanic, MoviePanicAdmin)
xadmin.site.register(TvMLS, TvMLSAdmin)
xadmin.site.register(TvMLSNoe, TvMLSNoeAdmin)
xadmin.site.register(TvJSK, TvJSKAdmin)
xadmin.site.register(TvJSKNoe, TvJSKNoeAdmin)
xadmin.site.register(TvEA, TvEAAdmin)
xadmin.site.register(TvEANoe, TvEANoeAdmin)
xadmin.site.register(TvOverSeas, TvOverSeasAdmin)
xadmin.site.register(TvOverSeasNoe, TvOverSeasNoeAdmin)
xadmin.site.register(TvHKT, TvHKTAdmin)
xadmin.site.register(TvHKTNoe, TvHKTNoeAdmin)
xadmin.site.register(ComicJSK, ComicJSKAdmin)
xadmin.site.register(ComicJSKNoe, ComicJSKNoeAdmin)
xadmin.site.register(ComicML, ComicMLAdmin)
xadmin.site.register(ComicMLNoe, ComicMLNoeAdmin)
xadmin.site.register(ComicOther, ComicOtherAdmin)
xadmin.site.register(ComicOtherNoe, ComicOtherNoeAdmin)

