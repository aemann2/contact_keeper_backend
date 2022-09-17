from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializers
from .models import Contact

# Create your views here.

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(owner=user.id)