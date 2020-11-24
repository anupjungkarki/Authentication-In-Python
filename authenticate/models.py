from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=225)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# # To Create Proxy  models  here.
# class Profile(User):
#     class Meta:
#         proxy = True
#
#     def get_full_name(self):
#         return self.first_name + self.last_name
