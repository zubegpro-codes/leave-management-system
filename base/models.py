from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,)
    bio = models.TextField(blank=True)
    nin = models.CharField(max_length=11, null=True)
    position =models.CharField(max_length=11, null=True)
    phoneNo = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=250, null=True)
    avatar = models.ImageField(null=True, upload_to='images/', default='avatar.svg')
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)


    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return self.username  # Display the name of the user in the admin panel
#

class Leaves(models.Model):
    user = models.ForeignKey(CustomUser, related_name='reports', on_delete=models.SET_NULL, null=True, blank=True)
    employee_ID = models.CharField(max_length=250,null=False, blank=False)
    email = models.EmailField(unique=True, )
    phoneNo = models.CharField(max_length=11, null=True)
    position = models.CharField(max_length=200, null=True)
    manager = models.CharField(max_length=200, null=True)
    manager_email = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    leave_start = models.DateField(null=False)
    leave_end = models.DateField(null=False)
    leave_type = models.CharField(max_length=20, choices=[('vacation', 'Vacation'), ('sick', 'Sick'),('quitting', 'Quitting')], null=False)
    description = models.TextField(null=False, blank=True)
    status = models.CharField(max_length=20, choices=[('unapproved', 'Unapproved'), ('Approved', 'Approved'), ('Declined', 'Declined') ],
                              default='unapproved')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']
    def __str__(self):
        return self.title
    

class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True,null=True)
    leave = models.ForeignKey(Leaves, on_delete=models.SET_NULL, blank=True, null=True)
    presentAddres =models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.presentAddres

