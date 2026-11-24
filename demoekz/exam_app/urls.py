from django.urls import path
from . import views

urlpatterns = [
    path('services', views.ServiceView.as_view()),
    path('requests', views.RequestsView.as_view()),
    path('doctors', views.DoctorsView.as_view()),
    path('newdoctor', views.NewDoctorView.as_view(), name = "doctorform"),
    path('newrequest', views.NewRequestView.as_view(), name = "requestform"),
    path('comment', views.NewCommentView.as_view(), name = "commentform"),
    path('allcomment', views.AllCommentView.as_view()),

]
