from django.forms import ModelForm
from .models import Doctor, Request, Comment

class DoctorForm(ModelForm):
   class Meta:
       model = Doctor
       fields = '__all__'

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'