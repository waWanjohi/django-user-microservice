"""
    <== The API Endpoints ==>

    Two functions get called:

    A. user_list
        1. Get a list of all users.
        2. Post a new user
        3. Delete users

    B. user_detail
     Manipulate individual user model.
        ALLOWED METHODS:    
            1. GET => Gets the user details
            2. PUT => Updates the user details
            3. DETELE => Deletes the user details

  

    <== THE NewUserViewSet CLASS ==> 
    This API Endpoint allows users to be viewed, and edited

    THE FOLLOWING ATTEMPTS TO USE THE DEFAULT DJANGO REST API VIEW, WHICH HAS PROVED UNSUCCESFUL SO FAR

    THIS PIECE IS ACTUALLY NOT ESSENTIAL FOR THE API TO RUN, BUT BE SURE TO REMOVE THE ITS IMPLEMENTATION IN urls.py 
    ie:
    # these two lines here
    router = routers.DefaultRouter()
    router.register(r'users', views.NewUserViewSet)

    # and the path in url_patterns = [
        path('auth/', include('rest_framework.urls')),
        ]
"""


from .models import NewUser
from rest_framework import viewsets
from .serializers import NewUserSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):

    if request.method == 'GET':
        users = NewUser.objects.all()

        newuser_serializer = NewUserSerializer(users, many=True)
        return JsonResponse(newuser_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        newuser_data = JSONParser().parse(request)
        newuser_serializer = NewUserSerializer(data=newuser_data)
        if newuser_serializer.is_valid():
            newuser_serializer.save()
            return JsonResponse(newuser_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(newuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = NewUser.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):

    try:
        user = NewUser.objects.get(id=id)

        # Retrieve a single object
        if request.method == 'GET':
            newuser_serializer = NewUserSerializer(user)
            return JsonResponse(newuser_serializer.data)

        # Update an object
        elif request.method == 'PUT':
            newuser_data = JSONParser().parse(request)
            newuser_serializer = NewUserSerializer(user, data=newuser_data)
            if newuser_serializer.is_valid():
                newuser_serializer.save()
                return JsonResponse(newuser_serializer.data)
            return JsonResponse(newuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete an object
        elif request.method == 'DELETE':
            user.delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

        #  Delete all objects
    except NewUser.DoesNotExist:
        return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)


class NewUserViewSet(viewsets.ModelViewSet):

    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
