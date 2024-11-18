from django.forms import ModelForm
from app.models import *

class EntryForm(ModelForm):
    class Meta:
        model= Entry
        fields= ('text', 'favorites')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["text"].widget.attrs.update({"class":"textarea","placeholder":"What\'s on your mind?(Please Use only 6 words to describe your day)"})
        self.fields["favorites"].widget.attrs.update({"class":"favorites"})