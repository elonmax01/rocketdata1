from django.db import models

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=5)

    def __str__(self):
        return self.country + ", " + self.city + ", " + self.street + ", " + self.house
    
class Factory(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Distributor(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Dealer(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def supplier(self):
        if self.distributor:
            return self.distributor
        elif self.factory:
            return self.factory
        else:
            return None
    
class Retailer(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def supplier(self):
        if self.dealer:
            return self.dealer
        elif self.distributor:
            return self.distributor
        elif self.factory:
            return self.factory
        else:
            return None

    
class IE(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, null=True, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def supplier(self):
        if self.retailer:
            return self.retailer
        elif self.dealer:
            return self.dealer
        elif self.distributor:
            return self.distributor
        elif self.factory:
            return self.factory
        else:
            return None
    

class Product(models.Model):
    plant = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    dealers = models.ManyToManyField(Dealer, blank=True)
    distributors = models.ManyToManyField(Distributor, blank=True)
    retailers = models.ManyToManyField(Retailer, blank=True)
    ies= models.ManyToManyField(IE, blank=True)
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
    
    def display_dealers(self):
        return ", ".join([dealer.name for dealer in self.dealers.all()])
    
    display_dealers.short_description = 'Dealers'

    def display_distributors(self):
        return ", ".join([distributor.name for distributor in self.distributors.all()])
    
    display_distributors.short_description = 'Distributors'

    def display_retailers(self):
        return ", ".join([retailer.name for retailer in self.retailers.all()])
    
    display_retailers.short_description = 'Retailers'

    def display_ies(self):
        return ", ".join([ie.name for ie in self.ies.all()])
    
    display_ies.short_description = 'IEs'

class Employee(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True, blank=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, null=True, blank=True)
    ie = models.ForeignKey(IE, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def display_company(self):
        companies = ''
        if self.factory:
            if companies != '':
                companies = companies + ', ' + self.factory.name
            else:
                companies = self.factory.name
        if self.distributor:
            if companies != '':
                companies = companies + ', ' + self.distributor.name
            else:
                companies = self.distributor.name
        if self.dealer:
            if companies != '':
                companies = companies + ', ' + self.dealer.name
            else:
                companies = self.dealer.name
        if self.retailer:
            if companies != '':
                companies = companies + ', ' + self.retailer.name
            else:
                companies = self.retailer.name
        if self.ie:
            if companies != '':
                companies = companies + ', ' + self.ie.name
            else:
                companies = self.ie.name
        return companies
    
    display_company.short_description = 'Company'

    