from django.db import models

# Create your models here.
class Plant(models.Model):
	Type = models.CharField(max_length =128, unique = True )
	Healthy = models.BooleanField()
	Symptom =  models.CharField(max_length =256, default="NIL")      
	PrevMeasure = models.CharField(max_length = 512, default = "NIL")

	# def __unicode__(self):
 #        return self.name


# class Symptoms(models.Model):
# 	Plant =  models.ForeignKey(Plant,
# 				on_delete=models.CASCADE,
# 				)
# 	Symptom =  models.CharField(max_length =256)      
# 	PrevMeasure = models.CharField(max_length = 512)

	# def __unicode__(self):
 #        return self.name