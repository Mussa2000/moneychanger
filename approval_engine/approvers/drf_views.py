
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import Approver
from .serializers import ApproverSerializer

# Create your views here.
class ApproverListAPIView(generics.ListAPIView):
    """
    Returns a list of all Approvers.
    """

    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApproverCreateAPIView(generics.CreateAPIView):
    """
    Create Approver.
    """

    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer


class ApproverDetailAPIView(generics.RetrieveAPIView):
    """
    Approver Detail
    """
    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer


class ApproverUpdateAPIView(generics.UpdateAPIView):
    """
    Update Approver.
    """

    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer


class ApproverDeleteAPIView(generics.DestroyAPIView):
    """
    Delete Approver.
    """

    queryset = Approver.objects.all()
    serializer_class = ApproverSerializer

