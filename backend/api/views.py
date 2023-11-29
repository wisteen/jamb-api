from django.shortcuts import render
# from django.http import JsonResponse
import json
from .models import Exam, Question, Subject
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import QuestionSerializer, UserSerializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def Jamb_api(request, *args, **kwargs):
    instances = Question.objects.all()
    data = {}

    if instances:
        serializer = QuestionSerializer(instances, many=True)
        data = serializer.data

    return Response(data)

@api_view(["POST"])
def login(request, *args, **kwargs):
	return Response({})

@api_view(["POST"])
def signup(request, *args, **kwargs):
	serializ = UserSerializers(data=request.data)
	if serializ.is_valid():
		serializ.save()
		user = User.objects.get(username=request.data['username'])
		user.set_password(request.data['password'])
		user.save()
		token = Token.objects.create(user=user)
		return Response({"token": token.key, "user":serializ.data})
	return Response(serializ.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def test_token(request, *args, **kwargs):
	return Response({})


# def api_zone(request, *args, **kwargs):
# 	body = request.body
# 	data = {}
# 	try:
# 		data = json.loads(body)
# 	except:
# 		pass
# 	data['headers'] = dict(request.headers)
# 	data['params'] = dict(request.GET)
# 	data['content_type'] = request.content_type
# 	print(data)
# 	return JsonResponse(data)


# def api_zone(request, *args, **kwargs):
# 	question_models = Question.objects.all().first()
# 	data ={}
# 	if question_models:
# 		data = model_to_dict(question_models)
# 	return JsonResponse(data)

