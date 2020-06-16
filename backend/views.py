from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Plant
from backend.serializers import PlantSerializer
import os
import tensorflow as tf
import keras as keras
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Create your views here.
def home(request):
    return render(request, 'backend/home.html', {})

@csrf_exempt
def List(request):
	if request.method == 'GET':
		plants = Plant.objects.all()
		serializer = PlantSerializer(plants, many=True)
		return JsonResponse(serializer.data, safe=False)

def readb64(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # if img is not None:
    #     h, w, _ = img.shape
    #     r = 640 / max(w, h)
    #     return cv2.resize(img, (int(w * r), int(h * r)))
    if img is not none:
    	return img

def main(base64Str):
    #model = get_file("model_formed.h5", pretrained_model, cache_subdir="pretrained_model",
    #                        file_hash=modhash, cache_dir=str(Path(__file__).resolve().parent))
    model_path = os.path.join(os.getcwd(), 'model_formed')
    # model_path = os.getcwd()
    model = tf.saved_model.load(model_path)
    img_list, expand_list, new_image1 = [], [], []
    image_dir = base64Str
    image_generator = readb64(image_dir)
    img = image_generator







    dict = {
    	'model_path' : model_path
    }
    return dict


@csrf_exempt
def Model(request):
    if request.method == 'GET':
        model = {}
        return JsonResponse(model, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        base64Str=data['img']
        return JsonResponse(main(base64Str), status=201)
