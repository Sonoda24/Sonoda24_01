from django.db import models

# Create your models here.
class My_Data(models.Model):
    # TODO: Define fields here
    no = models.IntegerField('番号', blank=True, null=True)
    theme = models.CharField('課題名', blank=True, max_length=30)
    bunrui1 = models.CharField('分類１', blank=True, max_length=30)
    bunrui2 = models.CharField('分類２', blank=True, max_length=30)
    bunrui3 = models.CharField('分類３', blank=True, max_length=30)
    day_regist = models.CharField('登録日', blank=True, max_length=30)
    day_modify = models.CharField('修正日', blank=True, max_length=30)
    overview = models.TextField('概要', blank=True)
    description = models.TextField('詳細', blank=True)
    keywords = models.TextField('KeyWd', blank=True)

    class Meta:
        verbose_name = '記録メモ'
        verbose_name_plural = '記録メモ一覧'

    def __unicode__(self):
        return(self.name)