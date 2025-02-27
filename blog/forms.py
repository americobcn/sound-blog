from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 max-w-xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )
    email = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "text-sm mx-2 my-3 px-2 max-w-xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "block text-sm mx-2 my-3 px-2 max-w-xl border-2 border-amber-400 text-gray-100 focus:outline-none focus:border-amber-300 focus:border-4 focus:bg-gray-800 rounded-md "
            }
        )
    )

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
