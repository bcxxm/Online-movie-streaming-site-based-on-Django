
# from django.conf.urls import url
from django.urls import path, re_path
from .import views

app_name = 'polltest'
urlpatterns = [
    path('', views.index, name='index'),
    path('paginator/', views.paginator, name='paginator'),
    re_path(r'^search/([\w\s@\[.【】 , 、，。; ‘ ’\+ \- “：= ！# ￥4$%……&*（）~^|(:\/s·{e}s_-f()\]{}\\]+)$',
            views.search, name='search'),
    path('hot/', views.hot, name='hot'),
    path('movie/', views.movie, name='movie'),
    re_path(r'^movie/(\w+)/$', views.movie_type, name='movie_type'),
    path('teleplay/', views.teleplay, name='teleplay'),
    path('QuickMark/', views.quickmark, name='quickmark'),
    re_path(r'^teleplay/(\w+)/$', views.teleplay_type, name='teleplay_type'),
    re_path(r'^comic/(\w+)/$', views.comic_type, name='comic_type'),
    path('comic/', views.comic, name='comic'),
    path('VarietyShow/', views.variety_show, name='variety_show'),
    # path('threed_movie/', views.threed_movie, name='threed_movie'),
    re_path(r'^(\w+)/(\d+)/$', views.search_play_context, name='search_play_context'),
    re_path(r'^(\w+)/(\w+)/(\d+)/$', views.play_context, name='play_context'),
    re_path(r'^play/(\w+)/(\w+)/(\d+)/play.html$', views.play, name='play'),
    re_path(r'^play/(\w+)/(\d+)/play.html$', views.search_play, name='search_play'),





]
