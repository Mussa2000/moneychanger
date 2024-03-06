from django.apps import AppConfig


class ApprovalGroupLevelsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "approval_engine.approval_group_levels"
    
    def ready(self) -> None:
        import approval_engine.approval_group_levels.signals
        return super().ready()
