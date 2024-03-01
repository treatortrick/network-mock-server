from django.db import models
from django.contrib.auth.models import User
from .base_models import BaseModel
from django.core.exceptions import ValidationError

# Create your models here.
class MockResponse(BaseModel):
    
    class Meta:
        verbose_name = verbose_name_plural = 'Mock IPI'

    REQUEST_METHOD = (
        ('GET', 'get'),
        ('POST', 'post'),
        ('PUT', 'put'),
        ('DELETE', 'delete'),
    )
        
    url = models.CharField(max_length=255, unique=True, verbose_name='url')
    response_data = models.JSONField(verbose_name='response', null=True, blank=True)
    delay_seconds = models.IntegerField(default=0, verbose_name='delay(s)')
    request_method = models.CharField(max_length=10, null=False, choices=REQUEST_METHOD, verbose_name='method')
    describe = models.CharField(max_length=255, verbose_name='describe', null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="creator")
    enable = models.BooleanField(default=True, verbose_name='enabled')
    
    
    def clean(self):
        if not self.url.startswith('/'):
            raise ValidationError('Please enter a valid URL. For example: /test/xxx.')
        if self.delay_seconds < 0 or self.delay_seconds > 180:
            raise ValidationError('The delay range must be between 0 and 180.')
    
    def pre_url(self):
        return 'https://yourhost/mock/test' + self.url
    pre_url.short_description = 'Actual URL'
    