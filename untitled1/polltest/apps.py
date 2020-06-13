# _*_ encoding:utf-8 _*_
from django.apps import AppConfig


class PolltestConfig(AppConfig):
    name = 'polltest'
    # app_icon = 'fa fa-camera-retro'
    verbose_name = u"电影列表"
    app_icon = 'fa fa-camera-retro'
    verbose_name_plural = verbose_name


default_app_config = "polltest.apps.PolltestConfig"