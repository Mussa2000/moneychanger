from django.apps import AppConfig


class ApprovalMarksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "approval_engine.approval_marks"
    
    def ready(self) -> None:
        import approval_engine.approval_marks.signals
        return super().ready()
