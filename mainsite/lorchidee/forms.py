from django import forms


class DateForm(forms.Form):
    """   """

    planningDate = forms.DateField(
        label='Date de la tournée:',
        widget=forms.TextInput(
            attrs={
                'label': "Trucy",
                'class': 'form-control',
                'type': 'date',
        })
    )

    file = forms.FileField(
        label='Choisir le fichier PDF:',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'type': 'file',
        })
    )
