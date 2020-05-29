from django.db import models
from django.core import validators

# Create your models here.
"""
class SubWeapon(models.Model):
    # TODO: Define fields here
    name = models.CharField('名前', blank=True, max_length=100)
    overview = models.TextField('概要', blank=True)


    class Meta:
        verbose_name = 'サブウェポン'
        verbose_name_plural = 'サブウェポン一覧'

    def __str__(self):
        return(self.name)


class Special(models.Model):
    # TODO: Define fields here
    name = models.CharField('名前', blank=True, max_length=100)
    overview = models.TextField('概要', blank=True)

    class Meta:
        verbose_name = 'スペシャル'
        verbose_name_plural = 'スペシャル一覧'

    def __str__(self):
        return(self.name)
"""
class article(models.Model):
    # TODO: Define fields here
    theme = models.CharField('課題名', blank=True, max_length=30)
    bunrui1 = models.CharField('大分類', blank=True, max_length=30)
    bunrui2 = models.CharField('中分類', blank=True, max_length=30)
    bunrui3 = models.CharField('小分類', blank=True, max_length=30)
    overview = models.CharField('概要', blank=True, max_length=200)

    def __unicode__(self):
        return(self.name)
    
"""    
    category = models.CharField(blank=True, max_length=2, choices=CATEGORY)
    sub = models.ForeignKey(SubWeapon, on_delete=models.PROTECT, null=True, blank=True)
    special = models.ForeignKey(Special, on_delete=models.PROTECT, null=True, blank=True)
    gauge = models.IntegerField('スペシャル必要ポイント', blank=True, null=True)
    release_condition = models.CharField('解放条件', blank=True, max_length=100)
    range = models.IntegerField('射程', blank=True, null=True)
    continuous_power = models.IntegerField('連射力', blank=True, null=True)
    fixed_num = models.IntegerField('確定数', blank=True, null=True)

    class Meta:
        verbose_name = 'ブキ'
        verbose_name_plural = 'ブキ一覧'
"""
