from django import forms

class FileForm(forms.Form):
    CHOICES = [
        ('aac', 'AAC'),
        ('wav', 'WAV'),
        ('flv', 'FLV'),
        ('mp3', 'MP3'),
        ('mp4', 'MP4'),
        ('ogg', 'OGG'),
    ]
    file = forms.FileField(label="File 1: ",required=False)
    format1 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )
    
    file2 = forms.FileField(label="File 2: ",required=False)
    format2 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file3 = forms.FileField(label="File 3: ",required=False)    
    format3 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file4 = forms.FileField(label="File 4: ",required=False)
    format4 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file5 = forms.FileField(label="File 5: ",required=False)
    format5 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file6 = forms.FileField(label="File 6: ",required=False)
    format6 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file7 = forms.FileField(label="File 7: ",required=False)
    format7 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )

    file8 = forms.FileField(label="File 8: ",required=False)
    format8 = forms.ChoiceField(label="New format:",
        widget=forms.RadioSelect,
        choices=CHOICES, )
    

    
    #format1= forms.CharField(label=)
    #= forms.CharField(label="New format: ")
