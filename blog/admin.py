from blog.models import Post
from django.contrib import admin
from django import forms
from django.db import models
from suit_ckeditor.widgets import CKEditorWidget

class PostAdmin(admin.ModelAdmin):
  formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

  class Media:
    js = {'ckeditor/ckeditor.js'}

admin.site.register(Post, PostAdmin)
