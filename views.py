from django.shortcuts import render
from rest_framework.views import APIView
from models import login
from models import register
from serializers import *
from rest_framework.response import Response

# Create your views here.

class AddMember(APIView):
	def dispatch(self,request,*args,**kwargs):
		return super(AddMember,self).dispatch(request,*args,**kwargs)

	def get(self,request,format=None):
		ob1 = login.objects.all().order_by('name')
		log = MemberPutSerializer(ob1,many=True)
		return Response(log.data)

	def post(self,request,format=None):
		data = request.data
		ob1 = MemberSerializer(data=data)
		if not ob1.is_valid():
			err = {}
			err['msg'] = ob1.errors
			#code = status.HTTP_400_BAD_REQUEST
			return Response(err)
		ob2 = login()
		ob2.name = data['name']
		ob2.mobile = data['mobile']
		ob2.save()
		log = MemberPutSerializer(ob2)
		return Response(log.data)



class UpdateMember(APIView):
	def dispatch(self,request,*args,**kwargs):
		return super(UpdateMember,self).dispatch(request,*args,**kwargs)


	def get(self,request,id,format=None):
		ob1 = login.objects.get(id=id)
		ob2 = MemberSerializer(ob1)
		return Response(ob2.data)

	def put(self,request,id,format=None):
		data = request.data
		ob1 = MemberSerializer(data=data)
		if not ob1.is_valid():
			err = {}
			err['msg'] = ob1.errors
			#code = status.HTTP_400_BAD_REQUEST
			return Response(err)
		ob2 = login.objects.get(id=id)
		ob2.name = data['name']
		ob2.mobile = data['mobile']
		ob2.save()
		ob3 = MemberPutSerializer(ob2)
		return Response(ob3.data)



class AddRegister(APIView):
	def dispatch(self,request,*args,**kwargs):
		return super(AddRegister,self).dispatch(request,*args,**kwargs)
	
	def get(self,request,lid,format=None):
		ob1 = register.objects.get(id=lid)
		ob2 = RegisterSerializer(ob1)
		return Response(ob2.data)

	def post(self,request,lid,format=None):
		ob1 =login.objects.get(id=lid)
		if ob1:
			data = request.data
			ser = RegisterSerializer(data=data)
			if not ser.is_valid():
				err = {}
				err['msg'] = ser.errors
				return Response(err)
			ob2 = register()
			ob2.login_id = lid
			ob2.college = data['college']
			ob2.spec = data['spec']
			ob2.save()
			ob3 = RegisterSerializer(ob2)
			return Response(ob3.data)
		err = {}
		err['msg'] = ob1.errors
		return Response(err)
		
