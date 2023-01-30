from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from IhaApp.models import User, Iha
from IhaApp.serializers import UserSerializer, IhaSerializer

# Create your views here.
def Index(request):
    return render(request, 'Index.html')
@csrf_exempt
def userLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(UserName = username, Password = password)
        
        if user is not None:
            return JsonResponse("Login is successfull", safe=False)
    else:
        return render(request, 'index.html')
@csrf_exempt
def userRegister(request):
    if request.method == 'POST':
        fname = request.Post['firstname']
        lname = request.Post['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create(UserName = username, FirstName = fname, LastName = lname, Password = password, Email = email )
        user_serializer = UserSerializer(data=user)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Registration is successful!", safe=False)
        return JsonResponse("Registration could not complete, please check your credentials.",safe=False)
@csrf_exempt
def ihaApi(request, id = 0):
    if request.method == 'GET':
        iha = Iha.objects.all()
        iha_serializer = IhaSerializer(iha, many=True)
        return JsonResponse(iha_serializer.data,safe=False)
    elif request.method == 'POST':
        iha_data = JSONParser().parse(request)
        iha_serializer= IhaSerializer(data=iha_data)
        if iha_serializer.is_valid():
            iha_serializer.save()
            return JsonResponse("Iha is added successfully", safe=False)
        return JsonResponse("Failed to add new iha", safe=False)
    elif request.method == 'PUT':
        iha_data = JSONParser().parse(request)
        iha = Iha.objects.get(IhaId=iha_data['IhaId'])
        iha_serializer= IhaSerializer(iha, data=iha_data)
        if iha_serializer.is_valid():
            iha_serializer.save()
            return JsonResponse("Iha is updated successfully!", safe= False)
        return JsonResponse("Failed to update")
    elif request.method== 'DELETE':
        iha=Iha.objects.get(IhaId = id)
        iha.delete()
        return JsonResponse("Iha is deleted successfully", safe=False)

