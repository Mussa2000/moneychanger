from django.apps import AppConfig


class ApprovalGroupMarksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "approval_engine.approval_group_marks"
    
    def ready(self) -> None:
        import approval_engine.approval_group_marks.signals
        return super().ready()
