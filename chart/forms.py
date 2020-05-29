# chart/forms.py

from django import forms
from .models import Chart

class ChartWriteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ChartWriteForm, self).__init__(*args,**kwargs)
        self.fields['title'].label = '차트 이름'
        self.fields['title'].widget.attrs.update({
            'placeholder' : '차트 이름',
            'autofocus' : True,
        })
    
    class Meta:
        model = Chart
        fields = ['chart_title','chart_url','chart_rank']
