######################## function based views ######################
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .serializers import UsersSerializer
from .models import Users
from rest_framework.decorators import api_view

# List or delete all users, or create a new user
@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):
    if request.method == 'GET':
        allUsers = Users.objects.all().order_by('username')

        users_serializer = UsersSerializer(allUsers, many=True)
        return JsonResponse(users_serializer.data, safe=False)
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Users.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
# Retrieve, update or delete a user
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try: 
        user = Users.objects.get(pk=pk) 
    except Users.DoesNotExist: 
        return JsonResponse({'message': 'The users does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UsersSerializer(user) 
        return JsonResponse(user_serializer.data) 
 
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        user_serializer = UsersSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        user.delete() 
        return JsonResponse({'message': 'user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)