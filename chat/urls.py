
from django.urls import path
from chat import views

urlpatterns = [
    path('', views.ListGroupView.as_view(), name='index'),
    path('messages/group/<int:pk>', views.DetailGroupView.as_view(), name='messages_group'),
    path('join_or_exit/group/<int:pk>', views.JoinExitGroupView.as_view(), name='join_or_exit_group'),
    path('add/message/<int:pk>', views.add_message_to_group, name='add_message')
]