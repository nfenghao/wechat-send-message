from django.db import models


# Create your models here.

class Userinfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    # blank是针对表单的,如果blank为true,表示在表单中该数据可以为空,且不影响数据库
    wexin_id = models.CharField(max_length=32, null=True, blank=True)
