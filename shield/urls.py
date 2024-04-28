from django.urls import path, include
from shield.views import(
    FolderListView,
    FolderCreateView,
    FolderUpdateView,
    FolderDetailsView,
    FolderDeleteView,
    
    DocumentListView,
    DocumentCreateView,
    DocumentUpdateView,
    DocumentDetailsView,
    DocumentDeleteView,
    DocumentDownloadView
)

urlpatterns = [
    path('folder/index/',FolderListView.as_view(), name="folder-index"), 
    path('folder/create/', FolderCreateView.as_view(), name="folder-create"),  
    path('folder/update/<int:pk>/', FolderUpdateView.as_view(), name="folder-update"), 
    path('folder/details/<int:pk>/', FolderDetailsView.as_view(), name="folder-details"), 
    path('folder/delete/<int:pk>/',FolderDeleteView.as_view(), name="folder-delete"), 
    
    path('document/index/',DocumentListView.as_view(), name="document-index"), 
    path('document/create/<int:pk>/', DocumentCreateView.as_view(), name="document-create"),  
    path('document/update/<int:pk>/', DocumentUpdateView.as_view(), name="document-update"), 
    path('document/details/<int:pk>/', DocumentDetailsView.as_view(), name="document-details"), 
    path('document/delete/<int:pk>/', DocumentDeleteView.as_view(), name="document-delete"), 
    path('document/download/<int:pk>/', DocumentDownloadView.as_view(), name="document-download"), 

]
