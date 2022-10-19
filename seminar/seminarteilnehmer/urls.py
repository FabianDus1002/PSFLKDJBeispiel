from django.urls import path
from . import views

urlpatterns = [
    path('teilnehmer', views.getAll),
    path('teilnehmer/<int:teilnehmer_id>', views.getOne),
    path('addteilnehmer', views.post),
    path('deleteteilnehmer/<int:teilnehmer_id>', views.delete),
    path('pupdate/<int:teilnehmer_id>', views.patch),
    path('update/<int:teilnehmer_id>', views.put),
]