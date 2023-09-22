from django import forms
from .views import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, CustomUser  # Assuming your Post model is imported

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'header_image' : forms.FileInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'tags' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):

    # This is way to apply styling to password fields or we can use __init__ method as defined below

    # password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
    

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add your comment here'}),
        }
        



# class PostUpdationForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ('author',)

#         widgets = {
#             'title' : forms.TextInput(attrs={'class': 'form-control'}),
#             'header_image' : forms.FileInput(attrs={'class': 'form-control'}),
#             'tags' : forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'status' : forms.Select(attrs={'class': 'form-control'}),
        # }


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('image',)

# class ImageFormset(forms.formsets.BaseFormSet):
#     form_class = ImageForm