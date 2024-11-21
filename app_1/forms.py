
from django import forms
from .models import Book,Category

class book_form(forms.ModelForm): # type: ignore
    
    class Meta:
        model = Book
        fields =[
            'title',
            'author',
            'photo',
            'photo_author',
            'pages',
            'price',
            'retal_price',
            'retal_period_type',
            'status',
            'category'
        ]
        widgets = {
         
         'title': forms.TextInput(attrs={'class':'form-control'}),
         'author': forms.TextInput(attrs={'class':'form-control'}),
         'photo': forms.FileInput(attrs={'class':'form-control'}),
         'photo_author': forms.FileInput(attrs={'class':'form-control'}),
         'pages': forms.NumberInput(attrs={'class':'form-control'}),
         'price': forms.NumberInput(attrs={'class':'form-control'}),
         'retal_price': forms.NumberInput(attrs={'class':'form-control'}),
         'retal_period_type': forms.Select(attrs={'class':'form-control'}),
         'status': forms.Select(attrs={'class':'form-control'}),
         'category': forms.Select(attrs={'class':'form-control'})
    }
class cata_form(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
