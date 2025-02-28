from django.contrib import admin
from .models import *
from django.db import models
from ckeditor.widgets import CKEditorWidget
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
admin.site.register(Post, PostAdmin)

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Tag)