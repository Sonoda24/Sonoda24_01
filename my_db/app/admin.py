from django.contrib import admin
from .models import article

# Register your models here.

@admin.register(article)
class ItemAdmin(admin.ModelAdmin):
    pass
