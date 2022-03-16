from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework .response import Response
from django.conf import settings
from Connectme.settings import DB
from rest_framework import status
import jwt 
from django.contrib.auth import authenticate
from utils import AuthAPIView
from utils.custom_id import generate_new_id



key = 'aaaa'
class Login(APIView):
    def get(self,request):
        pass

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        users_collection = DB["users"]
        print('---------------------------')
        user_username_password = users_collection.find_one({'username':username,'password':password})
        print('nnnnnnnnnnnnnnnn')

        if user_username_password is not None:
            payload = {
                'username':username,
                'password':password
            }
            jwt_encode = jwt.encode(payload, key)
            data = {
                'msg' : 'signedup successfully',
                'token' : jwt_encode,
                'username': user_username_password.get('username'),
                'password' : user_username_password.get('password')
            }
            print('lllllllllllllllll')
            return Response(data,status = status.HTTP_200_OK)
        else:
            data = {
                'msg':'please provide correct credentials'
            }
            return Response(data,status = status.HTTP_400_BAD_REQUEST)

class UserListView(AuthAPIView):
    def get(self,request):
        users_collection = DB["users"]
        data = list(users_collection.find({},{'_id': 0}))
        return Response(data)


class UserDetailView(AuthAPIView):
    def get(self,request,id):
        users_collection = DB["users"]
        data = users_collection.find_one({"id":id},{'_id': 0})
        print('88888888',request.user)
        return Response(data)




class Signup(APIView):


    def post(self,request):
        resp = ""
        username = request.data.get('username')
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')
        users_collection = DB["users"]
        id = generate_new_id(users_collection)
        my_input = {'username':username,'name':name,
                                            'email': email,'phone':phone,'password': password , 'id':id}
        find_mine = users_collection.find_one(my_input)
        if find_mine is None:
            users_data = users_collection.insert_one(my_input)
            resp= "user created successfully"
        else:
            resp= "user with this credentisla already present"

        return Response({"response":resp})

        def put(self,request):

            users_collection = DB["users"]
            pass

            pass





