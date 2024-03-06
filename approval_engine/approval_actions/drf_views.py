
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalAction
from .serializers import ApprovalActionSerializer

# Create your views here.
class ApprovalActionListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalActions.
    """

    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalActionCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalAction.
    """

    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer


class ApprovalActionDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalAction Detail
    """
    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer


class ApprovalActionUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalAction.
    """

    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer


class ApprovalActionDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalAction.
    """

    queryset = ApprovalAction.objects.all()
    serializer_class = ApprovalActionSerializer

