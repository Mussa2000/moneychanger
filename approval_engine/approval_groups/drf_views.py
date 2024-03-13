
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalGroup
from .serializers import ApprovalGroupSerializer

# Create your views here.
class ApprovalGroupListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalGroups.
    """

    queryset = ApprovalGroup.objects.all()
    serializer_class = ApprovalGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalGroupCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalGroup.
    """

    queryset = ApprovalGroup.objects.all()
    serializer_class = ApprovalGroupSerializer


class ApprovalGroupDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalGroup Detail
    """
    queryset = ApprovalGroup.objects.all()
    serializer_class = ApprovalGroupSerializer


class ApprovalGroupUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalGroup.
    """

    queryset = ApprovalGroup.objects.all()
    serializer_class = ApprovalGroupSerializer


class ApprovalGroupDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalGroup.
    """

    queryset = ApprovalGroup.objects.all()
    serializer_class = ApprovalGroupSerializer

