from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'editor'

    def ready(self):
        import editor.templatetags.custom_filters
