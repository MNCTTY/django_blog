from django.contrib import admin

# Register your models here.

# Чтобы наша модель стала доступна на странице администрирования, нам нужно зарегистрировать её при помощи admin.site.register(Post).
from .models import Post

admin.site.register(Post)
