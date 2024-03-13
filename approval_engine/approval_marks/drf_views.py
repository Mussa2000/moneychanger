
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalMark
from .serializers import ApprovalMarkSerializer

# Create your views here.
class ApprovalMarkListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalMarks.
    """

    queryset = ApprovalMark.objects.all()
    serializer_class = ApprovalMarkSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalMarkCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalMark.
    """

    queryset = ApprovalMark.objects.all()
    serializer_class = ApprovalMarkSerializer


class ApprovalMarkDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalMark Detail
    """
    queryset = ApprovalMark.objects.all()
    serializer_class = ApprovalMarkSerializer


class ApprovalMarkUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalMark.
    """

    queryset = ApprovalMark.objects.all()
    serializer_class = ApprovalMarkSerializer


class ApprovalMarkDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalMark.
    """

    queryset = ApprovalMark.objects.all()
    serializer_class = ApprovalMarkSerializer

