from dataclasses import fields
from .models import Transit,Booking
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    booking_id=serializers.ReadOnlyField()
    user=serializers.PrimaryKeyRelatedField()

    class Meta:
        model=Booking
        fields='__all__'