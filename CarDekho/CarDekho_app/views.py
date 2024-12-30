from django.shortcuts import get_object_or_404, render
from . models import *
from django.http import JsonResponse
from .api_file.serializers import *
from .api_file.permissions import AdminOrReadOnlyPermission, ReviewUserorReadonlypermission


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .api_file.throttling import ReviewlistThrottle, ReviewDetailThrottle
from .api_file.pagination import Reviewlistpagination, Reviewlistlimitoffpag, Reviewlistcursorpag


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializers

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        cars = Carlist.objects.get(pk=pk)
        useredit = self.request.user
        Review_queryset = Review.objects.filter(apiuser=useredit, car=cars)
        if Review_queryset.exists():
            raise ValidationError('You have already reviewed this car')
        serializer.save(car=cars, apiuser=useredit)

class Showroom_ViewSet(viewsets.ModelViewSet):
    queryset = Showroomlist.objects.all()
    serializer_class = ShowroomSerializer

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    # authentication_classes = [TokenAuthentication]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'review_list_scope'
    pagination_class = Reviewlistcursorpag
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(car=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    authentication_classes = [TokenAuthentication]
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'review_list_scope'
    permission_classes = [ReviewUserorReadonlypermission]



 

# class Showroom_ViewSet(viewsets.ViewSet):
#     def list(self, request):
#         showroom = Showroomlist.objects.all()
#         serializer = ShowroomSerializer(showroom, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = Showroomlist.objects.all()
#         showroom = get_object_or_404(queryset, pk=pk)
#         serializer = ShowroomSerializer(showroom)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = ShowroomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)



# class Showroom_View(APIView):
#     # authentication_classes = [SessionAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # permission_classes = [allowAny]
#     # permission_classes = [IsAdminUser]


#     def get(self,request):
#         showroom = Showroomlist.objects.all()
#         serializer = ShowroomSerializer(showroom, many=True, context={'request':request})
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ShowroomSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)
        
class Showroom_detail(APIView):
    def get(self,request,pk):
        try:
            showroom = Showroomlist.objects.get(pk=pk)
        except Showroomlist.DoesnotExist:
            return Response({'Error':'Showroom not found'},status=404)
        serializer = ShowroomSerializer(showroom,context={'request':request})
        return Response(serializer.data)
        
    def put(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        serializer = ShowroomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        showroom = Showroomlist.objects.get(pk=pk)
        showroom.delete()
        return Response(status=204)

        


@api_view(['GET', 'POST'])
def car_list(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT','DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response(status=404)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=204)