from django.contrib import admin
from django.apps import apps
# Register your models here.


app = apps.get_app_config('polls')
for model_name, model in list(app.models.items()):
    admin.site.register(model)