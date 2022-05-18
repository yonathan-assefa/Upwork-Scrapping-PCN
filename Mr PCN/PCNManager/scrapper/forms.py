import re
from django import forms


class PCNForm(forms.Form):
    pcn = forms.CharField(max_length=14, required=False)
    pcn_file = forms.FileField(required=False)

    #use bootstrap form
    def __init__(self, *args, **kwargs):
        super(PCNForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3 mr-sm-2'})


class EmailForm(forms.Form):
    email = forms.FileField(required=True)
    phone = forms.TextInput()
    # use bootstrap form
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3 mr-sm-2'})
