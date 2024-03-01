from django.urls import path
from .views import MockView

urlpatterns = [
    path('test/<path:url>', MockView.as_view(), name='mock_response'),

]