from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Ticket, Comment, User, Attachment
from .serializers import TicketSerializer, CommentSerializer, UserSerializer, AttachmentSerializer
from rest_framework.response import Response  
from rest_framework.generics import GenericAPIView

# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TicketStatsView(GenericAPIView):

    def get(self, request):
        open_count = Ticket.objects.filter(status='Open').count()
        closed_count = Ticket.objects.filter(status='Closed').count()
        
        return Response({
            'Open': open_count, 
            'Closed': closed_count
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer