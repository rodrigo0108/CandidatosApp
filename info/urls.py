from django.urls import path

from . import views

app_name = 'info'

urlpatterns = [
    path('', views.index, name='index'),
     # ex: /listado/
    path('listado', views.listado, name='listado'),
    # ex: /detalle/5/
    path('detalle/<int:candidato_id>/', views.detalle, name='detalle'),
]