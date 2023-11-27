from django import forms


class UserLoginForm(forms.Form):
    user = forms.TextField(
        widget=forms.TextInput(
            attrs={
                'id': 'username',
                'type': 'text',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'loginPassword',
                'type': 'password',
                'class': 'form-control'
            }
        )
    )
