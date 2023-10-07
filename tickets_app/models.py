from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.core.exceptions import ValidationError

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    phone_number = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    priority = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=[('Bug', 'Bug'), ('Feature Request', 'Feature Request'), ('Other', 'Other')])
    
    def __str__(self):
        return self.title
    
    def clean(self):
        if self.priority < 1 or self.priority > 5:
            raise ValidationError("La prioridad debe estar entre 1 y 5")
        
        if not self.title:
            raise ValidationError("El titulo no puede estar vacio")
        
        if self.category not in ['Bug', 'Feuture Request', 'Other']:
            raise ValidationError("La categoria debe ser Bug, Feature Request u Other")


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    description = models.CharField(max_length=255) 

