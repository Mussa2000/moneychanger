from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from helpers.appwrite_helpers import AppwriteDatabaseHandler
from appwrite.role import Role 
from appwrite.permission import Permission
from appwrite.exception import AppwriteException
from django.conf import settings


def create_update_remote_document(sender_model, get_user_id_func, assign_to_user=True):
    @receiver(post_save, sender=sender_model)
    def update_remote_document(sender, instance, created, **kwargs):
        if not created:
            appwrite_database_handler = AppwriteDatabaseHandler(
                database_id=instance.appwrite_database_id,
                collection_id=instance.appwrite_collection_id,
            )
            
            try:
                
                    
                appwrite_database_handler.update_document(
                    document_id=instance.appwrite_document_id,
                    data=instance.appwrite_payload,
                )
            except Exception as e:
                settings.LOGGER.error(f'{sender}: {e}')

    @receiver(post_save, sender=sender_model)
    def create_remote_document(sender, instance, created, **kwargs):
        if created:
            appwrite_database_handler = AppwriteDatabaseHandler(
                database_id=instance.appwrite_database_id,
                collection_id=instance.appwrite_collection_id,
            )
            
            permissions = None
            if assign_to_user:
                user_id = get_user_id_func(instance)
                permissions = [
                    Permission.read(
                        Role.user(user_id)
                    )
                ]
            try:
                settings.LOGGER.info(f'Creating {sender}: # {instance.appwrite_document_id}')
                response = appwrite_database_handler.create_document(
                    instance.appwrite_payload,
                    document_id=instance.appwrite_document_id,
                    permissions=permissions
                )
                
                instance.appwrite_document_id = response['$id']
                instance.save()
            except Exception as e:
                settings.LOGGER.error(f'{sender}: {e}')

    @receiver(post_delete, sender=sender_model)
    def delete_remote_document(sender, instance, **kwargs):
        appwrite_database_handler = AppwriteDatabaseHandler(
                database_id=instance.appwrite_database_id,
                collection_id=instance.appwrite_collection_id,
            )
        try:
            
                    
            appwrite_database_handler.delete_document(instance.appwrite_document_id)
        except Exception as e:
                settings.LOGGER.error(f'{sender}: {e}')
        
