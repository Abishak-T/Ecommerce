from django.contrib import admin
from app.models import SubModel,AppModel,SignupModel

# Register your models here.

admin.site.register(AppModel)
admin.site.register(SubModel)
admin.site.register(SignupModel)
