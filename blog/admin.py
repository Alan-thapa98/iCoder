from django.contrib import admin

# Register your models here.


from .models import  Post
from .models import  BlogComment
from .models import  BlogComment


admin.site.register(Post)
admin.site.register( BlogComment)
