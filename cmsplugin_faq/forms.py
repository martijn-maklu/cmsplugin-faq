from django.forms.models import ModelForm
#from cms.plugins.text.models import Text
from models import FaqEntry, FaqList
from django import forms


class FaqEntryForm(ModelForm):
    body = forms.CharField()
    
    class Meta:
        model = FaqEntry
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
        
#not needed because we're not allowing listing from other pages yet        
#class FaqListForm(ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(FaqListForm, self).__init__(*args, **kwargs)
#        if self.instance:
#            self.fields['cmspage'].queryset = FaqList.objects.filter(publisher_is_draft=True)