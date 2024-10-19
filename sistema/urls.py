from django.urls import path

from . import views

app_name = 'sistema'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:assunto_id>/", views.questionario, name="questionario"),
]