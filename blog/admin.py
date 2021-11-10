from django.contrib import admin
from .models import Post

# here is necessary to register the models of the app
admin.site.register(Post)

