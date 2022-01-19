from django import forms


class LaunchTaskForm(forms.Form):
    duration = forms.IntegerField(label='Duration in seconds', max_value=3600, min_value=0)
