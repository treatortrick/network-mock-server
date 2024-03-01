import os
from django.contrib import admin
from .models.mock_models import MockResponse

class MockResponseAdmin(admin.ModelAdmin):

    list_per_page=10
    actions_on_top = True
    
    
    """Searchable fields in the search box"""
    search_fields = ['url', 'describe']
    
    list_display = ['pre_url', 'describe', 'request_method', 'url', 'delay_seconds', 'enable', 'creator']
    
    """Non-editable fields on the page"""
    readonly_fields = ('creator',)
    
    exclude = ('is_deleted',)
    
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.creator = request.user
        obj.save()
        
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  
            return qs.filter(is_deleted=False)
        return qs.filter(creator=request.user, is_deleted=False)  

    def delete_model(self, request, obj):
        obj.is_deleted = True
        obj.save(update_fields=['is_deleted'])



admin.site.site_header = 'Work Branch'
admin.site.site_title = 'Work Branch'
admin.site.index_title = 'Work Branch'







admin.site.register(MockResponse, MockResponseAdmin)