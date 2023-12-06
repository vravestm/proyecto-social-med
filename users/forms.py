from django import forms


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
        })
    )


class UserSignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'signupEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        ))

    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control'
            }
        ))

    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        ))

    telefono = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'type': 'integer',
                'class': 'form-control'
            }
        ))

    nacionalidad = forms.ChoiceField(
        choices=[
            ('', 'Seleccione...'),
            ('española', 'Española'),
            ('extranjera', 'Extranjera'),
        ],
        widget=forms.Select(
            attrs={
                'class': ''}),
    )

    ciudad = forms.CharField(
        max_length=100,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    ocupacion = forms.CharField(
        max_length=100,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signupPassword',
                'type': 'password',
                'class': 'form-control'
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control'
            }
        ))

    # comprueba que el password2 es el requerido
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return cd['password2']
