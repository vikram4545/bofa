from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^number/$',views.NumberSerializerView.as_view()),
    url(r'^holder/$',views.HolderSerializerView.as_view())
]
