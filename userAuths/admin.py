from django.contrib import admin
from userAuths import models

admin.site.register(models.User)
admin.site.register(models.Profile)
