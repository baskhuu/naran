from django.apps import AppConfig
#adding class named BaseConfig
class BaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
