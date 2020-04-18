from django.contrib import admin
from blogContent.models import blogContents, commentContent

# Register your models here.
admin.site.register(blogContents)
admin.site.register(commentContent)