from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Plant
from backend.serializers import PlantSerializer

# Create your views here.
def home(request):
    return render(request, 'backend/home.html', {})

@csrf_exempt
def List(request):
	if request.method == 'GET':
		plants = Plant.objects.all()
		serializer = PlantSerializer(plants, many=True)
		return JsonResponse(serializer.data, safe=False)

# def symptomsList(request):
# 	if request.method == 'GET':
# 		symptoms = Symptoms.objects.all()
# 		serializer = SnippetSerializer(symptoms, many=True)
# 		return JsonResponse(serializer.data, safe=False)