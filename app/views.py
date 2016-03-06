from django.shortcuts import render
from django.http import HttpResponse
from app.serializers import UserSerializerGET, UserSerializerPOST, UserSerializerDetailGET, UserSerializerDetailPOST, SosSerializerGET, SosSerializerPOST, SosSerializerDetailGET, SosSerializerDetailPOST, SosSerializerStatusGET, SosSerializerStatusPOST

from app.models import user, sos 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import json,ast
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

#class JSONResponse(HttpResponse):
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['context_type'] = 'application/json'
#        super(JSONResponse,

@api_view(['GET','POST'])
def user_lookup(request):
    if request.method == 'GET':
        user_list = user.objects.all()
        serializer = UserSerializerGET(user_list,many=True)
        return Response(serializer.data, headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    elif request.method == 'POST':
        serializer = UserSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            out = { 'user_uuid': serializer.data['user_uuid'] }
            return Response(out, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def user_detail(request, pk):
    if request.method == 'GET':
        try:
            user_list = user.objects.get(user_uuid=pk)
            serializer = UserSerializerDetailGET(user_list)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    elif request.method == 'POST':
        serializer = UserSerializerDetailPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def sos_lookup(request):
    if request.method == 'GET':
        sos_list = sos.objects.all()
        serializer = SosSerializerGET(sos_list,many=True)
        return Response(serializer.data, headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    elif request.method == 'POST':
        serializer = SosSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            out = { 'sos_uuid': serializer.data['sos_uuid'] }
            return Response(out, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def sos_detail(request,pk):
    if request.method == 'GET':
        try:
            sos_list = sos.objects.get(sos_uuid=pk)
            serializer = SosSerializerDetailGET(sos_list)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    elif request.method == 'POST':
        serializer = SosSerializerDetailPOST(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            tmp = sos.objects.get(sos_uuid=pk)
            try:
                tmp_list = ast.literal_eval(tmp.location_list)
            except:
                tmp_list = [] 
            try:
                request_list = ast.literal_eval(request.data['location_list'])
            except:
                request_list = request.data['location_list']
            tmp_list.append(request_list[0])
            tmp.location_list = tmp_list
            tmp.save(update_fields=['location_list'])
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def sos_status(request,pk):
    if request.method == 'GET':
        try:
            sos_list = sos.objects.get(sos_uuid=pk)
            serializer = SosSerializerStatusGET(sos_list)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data,headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})
    elif request.method == 'POST':
        serializer = SosSerializerStatusPOST(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            try:
                tmp = sos.objects.get(sos_uuid=pk)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            tmp.status = request.data['status'] 
            tmp.save(update_fields=['status'])
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##def db(request):

    #greeting = Greeting()
    #greeting.save()

    #greetings = Greeting.objects.all()

    #return render(request, 'db.html', {'greetings': greetings})

