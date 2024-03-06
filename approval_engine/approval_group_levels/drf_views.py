
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalGroupLevel
from .serializers import ApprovalGroupLevelSerializer

# Create your views here.
class ApprovalGroupLevelListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalGroupLevels.
    """

    queryset = ApprovalGroupLevel.objects.all()
    serializer_class = ApprovalGroupLevelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalGroupLevelCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalGroupLevel.
    """

    queryset = ApprovalGroupLevel.objects.all()
    serializer_class = ApprovalGroupLevelSerializer


class ApprovalGroupLevelDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalGroupLevel Detail
    """
    queryset = ApprovalGroupLevel.objects.all()
    serializer_class = ApprovalGroupLevelSerializer


class ApprovalGroupLevelUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalGroupLevel.
    """

    queryset = ApprovalGroupLevel.objects.all()
    serializer_class = ApprovalGroupLevelSerializer


class ApprovalGroupLevelDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalGroupLevel.
    """

    queryset = ApprovalGroupLevel.objects.all()
    serializer_class = ApprovalGroupLevelSerializer

