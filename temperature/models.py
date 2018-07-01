from django.db import models

# Create your models here.
class Visitor(models.Model):
    visit_date = models.DateTimeField(auto_now=True)
    def get_date(self):
        return self.visit_date
