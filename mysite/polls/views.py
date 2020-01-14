from django.shortcuts import render

from django.http import HttpResponse

from .models import Truck, order


import logging

import grpc
import sys


import order_pb2_grpc
import order_pb2

def getRun(b):
	order = str(b)
	channel = grpc.insecure_channel('localhost:50051')
	stub = order_pb2_grpc.OrderStub(channel)
	response = stub.GetState(order_pb2.GetRequest(orderID=order))
	return response.answer

def setRun(b):
	order = str(b)
	channel = grpc.insecure_channel('localhost:50051')
	stub = order_pb2_grpc.OrderStub(channel)
	response = stub.SetState(order_pb2.SetRequest(orderID=order))
	return response.answer


def index(request):
	# logging.basicConfig()
	# res = setRun("4")
	data = Truck.objects.all()
	orders = order.objects.all()
	context = {'data': data, 'orders': orders}
	return render(request, 'polls/index.html', context)


def place(request):
	q = order(name = request.POST.get('name'))
	q.save()
	logging.basicConfig()
	res = setRun(q.id)
	output = "Your order, " + request.POST.get('choice') + ", " + res
	return HttpResponse(output)

def update(request):
	first = request.POST.get('user', False)
	q = order.objects.get(id = first)
	res = setRun(q.id)
	output = first + "'s order "  + res
	return HttpResponse(output)

def getStatus(request):
	first = request.GET.get('user')
	a = order.objects.get(id = first)
	# q = order.objects.get(name = request.POST.get('user', False))
	# res = getRun(q.id)
	# return HttpResponse(res)
	return HttpResponse(getRun(a.id))
