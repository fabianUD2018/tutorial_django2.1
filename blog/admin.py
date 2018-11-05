from django.contrib import admin
from .models import Post
# Register your models h-ere.

class PostConfig(admin.ModelAdmin):
    pass
admin.site.register(Post)