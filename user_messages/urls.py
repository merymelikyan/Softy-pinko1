from django.urls import path
from .views import receive_message

urlpatterns = [
    path('receive_message/', receive_message, name='receive_message'),
]




# from django.urls import path
# from . import views

# urlpatterns = [
#     path("send/", views.send_message, name= "send_message"),
#     path("sent/", views.message_sent, name= "message_sent"),
# ]
