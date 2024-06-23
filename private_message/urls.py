from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_items, name='sent_items'),
    path('send/', views.send_item, name='send_item'),
    path('archive/', views.archive, name='archive'),
    path('delete-message/<int:pk>/', views.delete_message, name='delete_message'),
    path('confirm-delete/<int:pk>/', views.item_confirm_delete, name='item_confirm_delete'),
    path('archive-message/<int:pk>/', views.archive_message, name='archive_message'),
    path('unarchive-message/<int:pk>/', views.unarchive_message, name='unarchive_message'),
    path('check-new-messages/', views.check_new_messages, name='check_new_messages'),
    path('<int:pk>/', views.view_item, name='view_item'),
]