from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from utils.local import _t


class UserProfile(AbstractUser):
    AUTHORITY = (
        ('DEV', '开发'),
        ('ADMIN', '管理'),
        ('BUSINESS', '商家'),
        ('CUSTOM', '顾客'),
        ('ANONYMOUS', '匿名'),
    )

    GENDER = (
        ("male", u"男"),
        ("female", "女")
    )

    user = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=GENDER, default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    authority = models.CharField(max_length=10, choices=AUTHORITY, default='CUSTOM', verbose_name='权限')

    class Meta:
        verbose_name = _t('用户')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
