from django.db import models

class BaseModel(models.Model):
    
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')    
    class Meta:
        abstract = True