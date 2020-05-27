# menu/forms.py

from django import forms
from .models import Menu

class MenuWriteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(MenuWriteForm, self).__init__(*args,**kwargs)
        self.fields['title'].label = '메뉴 이름'
        self.fields['title'].widget.attrs.update({
            'placeholder' : '메뉴 이름',
            'autofocus' : True,
        })
    
    class Meta:
        model = Menu
        fields = ['title','url','menu_rank']
