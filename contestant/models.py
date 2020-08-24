from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Account(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    paid     = models.BooleanField(default=False, blank=True, null=True)
    votes    = models.IntegerField(default=0, blank=False, null=False)
    phone    = models.CharField(blank=True, null=True, max_length=20)
    image    = models.FileField(upload_to='profile_images/', blank=True)
    voters   = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name

def create_account(sender, **kwargs):
    if kwargs['created']:
        account = Account.objects.create(user=kwargs['instance'])

post_save.connect(create_account, sender=User)
