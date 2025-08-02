from django.db import models
class Transcation(models.Model):
    date_t = models.DateField(max_length=200)
    amount_t = models.IntegerField()
    category_t = models.CharField(max_length=100)
    description_t = models.CharField(max_length=80)
    
    def __str__(self):
        return str(self.date_t)
    


