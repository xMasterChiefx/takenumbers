from django.urls import path
from . import views

app_name = 'takenumbers'

urlpatterns = [
    path('', views.index, name='home'),
    path('next/', views.nextnumber, name='nextnumber'),
    path('working/', views.workingnumber, name='workingnumber'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('working/<int:num_pk>', views.bncheck, name='bncheck'),
    path('dashboard/<int:num_pk>/archive', views.bnarchive, name='bnarchive'),
    path('working/<int:num_pk>/ready', views.bnready, name='bnready'),
    path('working/<int:num_pk>/delete', views.bndelete, name='bndelete'),
    path('working/alldelete', views.alldelete, name='alldelete'),
    path('working/takeout', views.takeout, name='takeout'),
    path('working/takeout/<int:num_pk>', views.takedelete, name='takedelete'),

]