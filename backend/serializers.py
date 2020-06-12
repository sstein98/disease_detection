from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plant
		fields =['Type','Healthy','Symptom','PrevMeasure']

# class SnippetSerializer1(serializers.ModelSerializer):		
# 	class Meta:
# 		model = Symptoms
# 		fields =['Plant','Symptom','PrevMeasure']