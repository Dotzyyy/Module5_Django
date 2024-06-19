from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_items, name='sent_items'),
    path('send/', views.send_item, name='send_item'),
    path('<int:message_id>/', views.view_item, name='view_item'),
]