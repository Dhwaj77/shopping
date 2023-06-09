from django.db import models
class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        return self.save()
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

