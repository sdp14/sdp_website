from django import forms
from models import Data, JSONModel, JSONModel_Tram

class DataForm(forms.ModelForm):

    class Meta:
        model = Data


class JSONModelForm(forms.ModelForm):

    class Meta:
        model = JSONModel
		
class JSONModel_Tram_Form(forms.ModelForm):

    class Meta:
        model = JSONModel_Tram		