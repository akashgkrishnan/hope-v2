from django.apps import AppConfig


class LeadConfig(AppConfig):
    name = 'lead'

    def ready(self):
        import lead.signals
    

