from django import forms


class LaunchWorkflowForm(forms.Form):
    type = forms.ChoiceField(label='Type of workflow', choices=[
        ('simple', 'Simple'),
        ('chain', 'Chain'),
    ])
    duration = forms.IntegerField(label='Duration in seconds', max_value=3600, min_value=0)
