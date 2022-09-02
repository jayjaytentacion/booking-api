from django.db import models
from accounts.models import CustomUser,Bookee
STATUS_CHOICES = (
    ("Boarded", "Boarded"),
    ("Missed", "Missed"),
    ("Unboarded","Unboarded"),
)

# Create your models here.


class Transit(models.Model):
    transit_id=models.CharField(max_length=28,unique=True)
    route=models.CharField(max_length=100)
    boarding_time=models.DateTimeField(auto_now_add=True)
    available_seats=models.IntegerField()
    price=models.IntegerField()

    # def __str__(self):
    #     return self.route + self.transit_id

class Booking(models.Model):
    booking_id=models.CharField( primary_key=True,max_length=7)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE ,blank=True,null=True)
    bookee=models.ForeignKey(Bookee,on_delete=models.CASCADE,default=user)
    transit=models.ForeignKey(Transit,on_delete=models.CASCADE)
    seat_number=models.IntegerField(unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    payment_ref=models.CharField(max_length=8)
    status=models.CharField(max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Unboarded')

    # def __str__(self):
    #     return self.user + self.bookee   






