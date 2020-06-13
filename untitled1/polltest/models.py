from django.db import models


class MovieHot(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MovieAction(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro

    class Meta:
        # db_table = 'MovieAction'
        verbose_name = "动作片"
        verbose_name_plural = verbose_name


class MovieComedy(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        # db_table = 'Movie'
        verbose_name = '喜剧片'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MovieLove(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "爱情片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MovieScience(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "科幻片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MoviePanic(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "恐怖片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MovieWar(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "战争片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


class MoviePlot(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    mv_url = models.CharField(max_length=100)
    mu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "剧情片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.pf, \
               self.tv_type, self.language, self.time, self.img_url,\
               self.mv_url, self.mu_url, self.isDisplay, self.intro


# 电视剧模型开始
class TvMainLand(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=40)
    star = models.CharField(max_length=100)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvMainLandNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    # tu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvMainLand, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.one_set, self.tv_url, self.isDisplay, self.tv_id


class TvMLS(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=150)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "大陆剧"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvMLSNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    # down_url = models.CharField(max_length=150)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvMLS, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "大陆剧子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class TvHKT(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=150)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "港台剧"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvHKTNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    # down_url = models.CharField(max_length=150)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvHKT, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "港台剧子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class TvEA(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "欧美剧"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvEANoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    # down_url = models.CharField(max_length=150, null=True)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvEA, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "欧美剧子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class TvJSK(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "日韩剧"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvJSKNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    # down_url = models.CharField(max_length=150)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvJSK, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "日韩剧子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class TvOverSeas(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "海外剧"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class TvOverSeasNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    # down_url = models.CharField(max_length=150)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(TvOverSeas, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "海外剧子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class ComicJSK(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "日韩动漫"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class ComicJSKNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    down_url = models.CharField(max_length=150, null=True)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(ComicJSK, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "日韩动漫子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class ComicML(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "大陆动漫"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class ComicMLNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    down_url = models.CharField(max_length=150, null=True)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(ComicML, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "大陆动漫子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class ComicOther(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "欧美动漫"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type,\
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class ComicOtherNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    down_url = models.CharField(max_length=150, null=True)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(ComicOther, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "欧美动漫子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id


class VarietyShow(models.Model):
    tv_name = models.CharField(max_length=40)
    noe = models.CharField(max_length=20)
    director = models.CharField(max_length=100)
    star = models.CharField(max_length=250)
    area = models.CharField(max_length=20)
    time = models.CharField(max_length=40)
    tv_type = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    pf = models.DecimalField(max_digits=4, decimal_places=2)
    intro = models.CharField(max_length=2000)
    imgurl = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "综艺"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tv_name, self.noe, self.star, self.director, self.tv_type, \
               self.language, self.time, self.pf, self.intro, self.img_url, self.isDisplay


class VarietyShowNoe(models.Model):
    one_set = models.CharField(max_length=40)
    tv_url = models.CharField(max_length=100)
    tu_url = models.CharField(max_length=100)
    isDisplay = models.SmallIntegerField(default=1)
    tv_id = models.ForeignKey(VarietyShow, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "综艺子表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.one_set, self.tv_url, self.tu_url, self.isDisplay, self.tv_id