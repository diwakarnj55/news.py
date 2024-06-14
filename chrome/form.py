from django import forms
from . models import Biznews

class BiznewsForm(forms.ModelForm):
    class Meta:
        model=Biznews
        fields =["biz_image","biz_date","biz_title"]
