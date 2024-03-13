
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalGroupAction
from .serializers import ApprovalGroupActionSerializer

# Create your views here.
class ApprovalGroupActionListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalGroupActions.
    """

    queryset = ApprovalGroupAction.objects.all()
    serializer_class = ApprovalGroupActionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalGroupActionCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalGroupAction.
    """

    queryset = ApprovalGroupAction.objects.all()
    serializer_class = ApprovalGroupActionSerializer


class ApprovalGroupActionDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalGroupAction Detail
    """
    queryset = ApprovalGroupAction.objects.all()
    serializer_class = ApprovalGroupActionSerializer


class ApprovalGroupActionUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalGroupAction.
    """

    queryset = ApprovalGroupAction.objects.all()
    serializer_class = ApprovalGroupActionSerializer


class ApprovalGroupActionDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalGroupAction.
    """

    queryset = ApprovalGroupAction.objects.all()
    serializer_class = ApprovalGroupActionSerializer

