from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return self.name + ' ' + self.surname


class Service(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    number = models.IntegerField(default=1)

    def __str__(self):
        return 'subscription of user ' + str(self.user)