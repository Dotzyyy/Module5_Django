from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_items, name='sent_items'),
    path('send/', views.send_item, name='send_item'),
    path('check-new-messages/', views.check_new_messages, name='check_new_messages'),
    path('<int:pk>/', views.view_item, name='view_item'),
]