from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .serializers import AddressesSerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
#from .faq_chatbot import faq_answer
from .blip2_chat import blip2_vqa
import random
import os

# Create your views here.s
@csrf_exempt
def main(request):
    return render(request,'v1/index.html')


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)



@csrf_exempt
def login(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')
        print("id = " + id + " pw = " + pw)

        result = authenticate(username=id, password=pw)

        if result :
            print("로그인 성공!")
            return HttpResponse(status=200)
        else:
            print("실패")
            return HttpResponse(status=401)


    return render(request, 'addresses/login.html')

@csrf_exempt
def app_login(request):

    if request.method == 'POST':
        print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid', '')
        pw = request.POST.get('userpw', '')
        print("id = " + id + " pw = " + pw)

        result = authenticate(username=id, password=pw)

        if result:
            print("로그인 성공!")
            return JsonResponse({'code': '0000', 'msg': '로그인성공입니다.'}, status=200)
        else:
            print("실패")
            return JsonResponse({'code': '1001', 'msg': '로그인실패입니다.'}, status=200)


@csrf_exempt
def chat_service(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        #file = request.FILES['image']
        #print(file.name)
        # response = '안녕'
        # response = faq_answer(input1)
        image_path = os.getcwd()+"\\media\\test\\test.jpg"
        response = blip2_vqa(input1, image_path)
        output = dict()
        output['response'] = response
        return HttpResponse(json.dumps(output), status=200)
    else:
        return render(request, 'addresses/chat_test.html')
    
@csrf_exempt
def image_upload(request):
    if request.method == 'POST':
        file = request.FILES['image']
        print(file.name)
        # 이미지 이름 바꾸기
        file.name = "test.jpg"
        # 폴더가 있으면 그냥 넘기고 없으면 생성하자
        fs = FileSystemStorage()
        # 이미 test.jpg가 있으면 기존 파일 삭제
        if fs.exists("test" + '/' + file.name):
            fs.delete("test" + '/' + file.name)

        fs.save("test" + '/' + file.name, file)
        return redirect('chat_service')
    else:
        form = ProductForm() # request.method 가 'GET'인 경우
    return render(request, 'addresses/chat_test.html')