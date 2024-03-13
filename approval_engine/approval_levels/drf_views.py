
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalLevel
from .serializers import ApprovalLevelSerializer

# Create your views here.
class ApprovalLevelListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalLevels.
    """

    queryset = ApprovalLevel.objects.all()
    serializer_class = ApprovalLevelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalLevelCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalLevel.
    """

    queryset = ApprovalLevel.objects.all()
    serializer_class = ApprovalLevelSerializer


class ApprovalLevelDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalLevel Detail
    """
    queryset = ApprovalLevel.objects.all()
    serializer_class = ApprovalLevelSerializer


class ApprovalLevelUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalLevel.
    """

    queryset = ApprovalLevel.objects.all()
    serializer_class = ApprovalLevelSerializer


class ApprovalLevelDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalLevel.
    """

    queryset = ApprovalLevel.objects.all()
    serializer_class = ApprovalLevelSerializer

