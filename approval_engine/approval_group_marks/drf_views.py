
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalGroupMark
from .serializers import ApprovalGroupMarkSerializer

# Create your views here.
class ApprovalGroupMarkListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalGroupMarks.
    """

    queryset = ApprovalGroupMark.objects.all()
    serializer_class = ApprovalGroupMarkSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalGroupMarkCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalGroupMark.
    """

    queryset = ApprovalGroupMark.objects.all()
    serializer_class = ApprovalGroupMarkSerializer


class ApprovalGroupMarkDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalGroupMark Detail
    """
    queryset = ApprovalGroupMark.objects.all()
    serializer_class = ApprovalGroupMarkSerializer


class ApprovalGroupMarkUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalGroupMark.
    """

    queryset = ApprovalGroupMark.objects.all()
    serializer_class = ApprovalGroupMarkSerializer


class ApprovalGroupMarkDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalGroupMark.
    """

    queryset = ApprovalGroupMark.objects.all()
    serializer_class = ApprovalGroupMarkSerializer

