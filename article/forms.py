from django import forms
from models import Article, File_Upload, Tram_File_Upload

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article


class File_UploadForm(forms.ModelForm):

    class Meta:
        model = File_Upload
		
		
class Tram_File_UploadForm(forms.ModelForm):

    class Meta:
        model = Tram_File_Upload		