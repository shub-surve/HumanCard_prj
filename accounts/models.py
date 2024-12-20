from django.db import models
from django.contrib.auth.models import User
import random 
import string


import random
import string
from django.db import models
from django.contrib.auth.models import User

class HumanCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    humancard_id = models.AutoField(primary_key=True , editable=False)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # New field for profile picture

    # def save(self, *args, **kwargs):
    #     if not self.humancard_id:
    #         random_3_num = ''.join(random.choices(string.digits, k=3))
    #         random_2_char = ''.join(random.choices(string.ascii_uppercase, k=2))
    #         random_4_num = ''.join(random.choices(string.digits, k=4))
    #         self.humancard_id = f'HUI{random_3_num}{random_2_char}{random_4_num}'
    #     super(HumanCard, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.user.username}'s HumanCard"

        



class Contact(models.Model):
    email = models.EmailField(max_length=254)
    query = models.TextField()
