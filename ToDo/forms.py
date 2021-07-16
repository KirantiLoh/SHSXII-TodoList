from django import forms

class CreateToDoForm(forms.Form):
    title = forms.CharField(max_length=50)

class CreateItemForm(forms.Form):
    content = forms.CharField(max_length=50)
    is_urgent = forms.BooleanField(required=False)

class SearchListForm(forms.Form):
    title_search = forms.CharField(max_length=50)