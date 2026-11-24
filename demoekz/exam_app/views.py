from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import *
from .forms import DoctorForm, RequestForm, CommentForm
from django.urls import reverse_lazy

class NewDoctorView(FormView):
    form_class = DoctorForm
    template_name = 'doctorform.html'
    success_url = reverse_lazy('doctorform')
    
class NewRequestView(FormView):
    form_class = RequestForm
    template_name = 'requestform.html'
    success_url = reverse_lazy('requestform')

class NewCommentView(FormView):
    form_class = CommentForm
    template_name = 'comments.html'
    success_url = 'allcomment'

class AllCommentView(ListView):
    model = Comment
    template_name = 'allcomments.html'
    context_object_name = 'allcomment'
    
class ServiceView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'
    paginate_by = 5

class DoctorsView(ListView):
    model = Doctor 
    template_name = 'doctor.html'
    context_object_name = 'doctors'
    paginate_by = 1
    
class RequestsView(ListView):
    model = Request 
    template_name = 'requests.html'
    context_object_name = 'requests'
    paginate_by = 1