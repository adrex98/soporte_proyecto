from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, CommentViewSet, TicketStatsView, UserViewSet, AttachmentViewSet
from pprint import pprint

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)
router.register('users', UserViewSet)
router.register('attachments', AttachmentViewSet)

pprint(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('ticket-stats/', TicketStatsView.as_view(), name='ticket-stats'),
]
