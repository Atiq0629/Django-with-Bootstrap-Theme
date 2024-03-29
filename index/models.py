from django.db import models

class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)
    
    def __str__(self):
        return self.title
    

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)
    
    def __str__(self):
        return self.title
    
    
class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)
    
    def __str__(self):
        return self.name
    
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

