from django.contrib import admin
from .models import *

# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserInfo)
admin.site.register(Goods)
admin.site.register(Brand)

