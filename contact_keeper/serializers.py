from pyexpat import model
from rest_framework import serializers
from .models import Contact

# serializer will convert our model instance to JSON so that the frontend can work with the received data
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'owner', 'name', 'email', 'phone', 'contact_type')