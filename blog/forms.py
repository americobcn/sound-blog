from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 max-w-xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 md:max-w-2xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        )
    )
    to = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 md:max-w-2xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        )
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "block text-sm mx-1 w-full my-3 px-2 md:max-w-2xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mb-3 px-2 border-2 border-slate-400 w-full text-gray-100 focus:outline-none focus:border-slate-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )
    email = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mb-3 px-2 border-2 border-slate-400 w-full text-gray-100 focus:outline-none focus:border-slate-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "block text-sm mx-auto mb-3 px-2 py-1 w-full border-2 border-slate-400 text-gray-100 focus:outline-none focus:border-slate-300 focus:border-4 focus:bg-gray-800 rounded-md"
            }
        )
    )

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
