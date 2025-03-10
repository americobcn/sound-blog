from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 max-w-xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 md:max-w-2xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        )
    )
