from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,
                               min_length=5, required=True, error_messages={
            "max_length": "用户名长度最长为20", "min_length": "用户名最少长度为5"})
    password = forms.CharField(max_length=20, min_length=8, required=True)
    password2 = forms.CharField(max_length=20, min_length=8, required=True)
    mobile = forms.CharField(max_length=11, min_length=11, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Two different passwords')
        return cleaned_data
