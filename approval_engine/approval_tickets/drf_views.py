
# DRF Views 
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import ApprovalTicket
from .serializers import ApprovalTicketSerializer

# Create your views here.
class ApprovalTicketListAPIView(generics.ListAPIView):
    """
    Returns a list of all ApprovalTickets.
    """

    queryset = ApprovalTicket.objects.all()
    serializer_class = ApprovalTicketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    # Fields to use when searching
    search_fields = []
    
    # Available ordering fields
    ordering_fields = []
    
    # default ordering field
    ordering = []
    
    # filters
    filterset_fields = []


class ApprovalTicketCreateAPIView(generics.CreateAPIView):
    """
    Create ApprovalTicket.
    """

    queryset = ApprovalTicket.objects.all()
    serializer_class = ApprovalTicketSerializer


class ApprovalTicketDetailAPIView(generics.RetrieveAPIView):
    """
    ApprovalTicket Detail
    """
    queryset = ApprovalTicket.objects.all()
    serializer_class = ApprovalTicketSerializer


class ApprovalTicketUpdateAPIView(generics.UpdateAPIView):
    """
    Update ApprovalTicket.
    """

    queryset = ApprovalTicket.objects.all()
    serializer_class = ApprovalTicketSerializer


class ApprovalTicketDeleteAPIView(generics.DestroyAPIView):
    """
    Delete ApprovalTicket.
    """

    queryset = ApprovalTicket.objects.all()
    serializer_class = ApprovalTicketSerializer

