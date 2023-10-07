from django.contrib import admin
from .models import Ticket, Comment, Attachment, User

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Attachment)
