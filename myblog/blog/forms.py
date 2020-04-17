from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm): #inherits from forms.ModelForm
    
    class Meta: #must in forms
        model = Post #model we are dealing with
        fields = ('author','title','text') #fields we need
    
    #widgets for editing the css inside the meta pass dictionary
        widgets = {#connecting our modelFormFields to css classes
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author','text')
        
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }