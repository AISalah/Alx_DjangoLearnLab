from django import forms

class ExampleForm(forms.Form):
    example_field = forms.CharField(label="Your Input", max_length=100)