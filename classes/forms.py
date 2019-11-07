from .models import Class
from django.forms import ModelForm


class ClassForm(ModelForm):

    class Meta:
        model = Class
        exclude = ('date_request', )
        fields = '__all__'