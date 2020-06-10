# chart/forms.py

from django import forms
from .models import Chart
from menu.models import Menu

class ChartWriteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ChartWriteForm, self).__init__(*args,**kwargs)
        self.fields['chart_title'].label = '차트 이름'
        self.fields['chart_title'].widget.attrs.update({
            'placeholder' : '차트 이름',
            'autofocus' : True,
        })
        self.fields['sheet_name'].label = '시트 이름'
        self.fields['sheet_name'].widget.attrs.update({
            'placeholder' : '시트 이름',
        })
        self.fields['sheet_name'] = forms.ModelChoiceField(
            queryset=Menu.objects.all()
        )
    
    class Meta:
        model = Chart
        fields = ['chart_title','sheet_name','chart_url','chart_rank']
