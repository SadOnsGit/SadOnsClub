from django import forms

from users.models import CustomUsers

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUsers
        fields = ['username', 'email', 'password', 'repeat_password']
        

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUsers.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Введенный вами Username уже занят.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUsers.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Введенный вами Email уже используется.")
        return email


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password  = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error("repeat_password", forms.ValidationError("Пароли не совпадают."))