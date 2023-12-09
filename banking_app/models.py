from django.db import models

# Create your models here.
class Branches(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Sub_Branches(models.Model):
    name = models.CharField(max_length=100)
    main_branch = models.ForeignKey(Branches,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
        # Add more choices as needed
    ]

    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(Branches, on_delete=models.CASCADE)
    branch = models.ForeignKey(Sub_Branches, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    materials_provided = models.ManyToManyField('Material', blank=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name