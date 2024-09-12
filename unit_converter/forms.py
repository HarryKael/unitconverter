from django import forms

class WeightConverter(forms.Form):
    WEIGHT_CHOICES = [
        ('Milimeter', 'Milimeter'),
        ('Centimeter', 'Centimeter'),
        ('Meter', 'Meter'),
        ('Inch', 'Inch'),
        ('Foot', 'Foot'),
        ('Yard', 'Yard'),
        ('Mile', 'Mile'),
    ]

    data = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    convert_from = forms.CharField(choices=WEIGHT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    convert_to = forms.CharField(choices=WEIGHT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    def convert(self):
        if self.is_valid():
            # Convert
            return True
        return False