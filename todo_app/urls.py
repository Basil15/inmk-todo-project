
from django.urls import path, include
from  . import views

urlpatterns = [

    path('',views.add, name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    #generic url
    path('generichomeview/',views.TastlistView.as_view(),name='generichomeview'),
    path('genericdetailview/<int:pk>/',views.Taskdetailview.as_view(),name='genericdetailview'),
    path('genericdupdate/<int:pk>/',views.TaskUpadate.as_view(),name='genericdupdate'),
    path('genericddelete/<int:pk>/',views.TaskDeleteView.as_view(),name='genericddelete'),

]
