from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    contact = models.CharField(max_length=9)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    model = models.CharField(max_length=30)
    year = models.DateField()
    plate = models.CharField(max_length=6)
    owner = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

class Checkout(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    out_date = models.DateTimeField()

    def __str__(self):
        return str(self.out_date)

class Checkin(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    in_date = models.DateTimeField()

    def __str__(self):
        return str(self.in_date)

