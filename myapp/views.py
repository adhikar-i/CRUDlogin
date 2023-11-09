
from .models import Viewer
from django.contrib.auth import authenticate, login
from .serializers import ViewerSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
#from rest_framework.models import Token
from rest_framework import status
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from myapp import serializers


# Create your views here.
class getData(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
#@api_view(['GET'])
    def get(self, request):
        name = Viewer.objects.all()
        nameSerializer = ViewerSerializer(name, many=True)
        return Response(nameSerializer.data) 

class addViewer(APIView):
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
#@api_view(['POST'])
    def post(self, request):
        try:
            serializer = ViewerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
           
                return Response({'message': 'Registration Succesful'}, status=status.HTTP_200_OK)
       
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':'Exception occured:{}'.format(str(e))},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class getViewer(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
#@api_view(['POST'])
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return Response({'detail': 'Logged in'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        #return Response({'message': 'Login Succesful'}, status=200)
    #print(Username)
    #print(Password)
    #return Response({'message': 'login failed'}, status=401)

class updateData(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]   
#@api_view(['PUT'])
    def put(self, request, id):
        try:
            name = Viewer.objects.get(pk=id)
        except Viewer.DoesNotExist:
            return Response({'message': 'Name not found'}, status=404)
    
        serializers = ViewerSerializer(name, data=request.data)
        if serializers.is_valid():
            serializers.save()
            print("Data Updated succesfully")
            return Response(serializers.data)
        print("Validation errors:", serializers.data)
        return Response(serializers.errors, status=400)

class deleteData(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
#@api_view(['DELETE'])
    def delete(self, request, id):
        try:
            name = Viewer.objects.get(pk=id)
        except Viewer.DoesNotExist:
            return Response({'message': 'Employee not found'}, status=404)
        name.delete()
        return Response({'message': 'Employee deleted successfully'}, status=204)
