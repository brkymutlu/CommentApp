from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    full_name = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    # blank = True -> Alanın zorunlu olarak yazılmasını engeller.
    # null = True -> Alanın boş geçilebilir olmasını sağlar.

    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    def __str__(self):
        return self.full_name
    
