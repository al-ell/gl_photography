from django import forms
from crispy_forms.helper import FormHelper
from .models import Project, Photo


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description',]

    placeholders = {
        'name': 'Project Name',
        'description': 'Description',
    }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
    

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['project', 'name', 'friendly_name', 'image_url', 'description',]

    image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        projects = Project.objects.all()


    placeholders = {
        'project': 'Project',
        'name': 'Name',
        'friendly_name': 'Public Name',
        'description': 'Description',
    }

    

