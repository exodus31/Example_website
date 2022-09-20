from django.db import models

# Create your models here.

class Objects(models.Model):
    geography = models.CharField(max_length=100, default="The Geography of Asgard is dominated by huge mountains.")
    history = models.CharField(max_length=100, default="History of Asgard goes back a millenia.")
    culture = models.CharField(max_length=100, default="Culturally Asgard remains a mystery to the passer by")
    language = models.CharField(max_length=100, default="Language barriers in Asgard do not allow outsiders to live.")
