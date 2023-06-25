
from datetime import timedelta, timezone
from http.client import responses
import json
from typing import Self
from django.contrib.auth import authenticate, logout 
from django.http import JsonResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
# from HSBZ4.settings import GOOGLE_MAPS_API_KEY
# from account import serializers
from account.forms import *
from django.http import JsonResponse
from django.db.models import Q

from api.renderers import UserRenderer
from .serializers import AuthTokenSerializer, CustomUserSerializer,AddressSerializer, CoustSerializer, LoginSerializer, CoustemSectionSerializer, OrderDitilessiSerializer, OrderDitilessiSerializer, OrdersSerializer, ProdectSerializer, TypeCoustSerializer, UserLoginSerializer, UserSerializer, UsersSerializer
# Create your views here.
from account.models import CustomUser,TypeAccount
from django.contrib.auth.decorators import login_required
from prodect.models import *
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import api_view

from order.models import *
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAuthorOrReadOnly
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from .utils import get_and_authenticate_user

from django.contrib.auth.hashers import make_password
from functools import reduce
import operator
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib import messages
from account.forms import *
from order.forms import *
from prodect.forms import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
############################################## jwt authantcion 
from django.conf import settings
import jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

jwt_payload_handler = TokenObtainPairSerializer()
jwt_encode_handler = TokenObtainPairSerializer()
# from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


  
class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logins(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        jwt_payload_handler = settings.SIMPLE_JWT['JWT_PAYLOAD_HANDLER']
        jwt_encode_handler = settings.SIMPLE_JWT['JWT_ENCODE_HANDLER']
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request):
    serializer = UsersSerializer(request.user)
    return Response(serializer.data)






# class UserChangePassowrdView(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request,format=None):
#         serializer=UserChangePassowrdSerializer(data=request.data,context={'user':request.user},status=status.HTTP_400_BAD_REQUEST)
#         if serializer.is_valid(raise_exception=True):
#             return Response({'msg':'passowrd change sucssfly'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('username')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)








##########################################################
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             messages.add_message(request, messages.SUCCESS, 'تم تسجيل الدخول بنجاح')
#             return Response({'token': token.key})
#         else:
#             messages.add_message(request, messages.ERROR, 'فشل تسجيل الدخول')
#             return Response({'error': 'Invalid credentials'})
#######################
class UserRegistrationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.permissions import IsAuthenticated
# class LoginAPI(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user'] # type: ignore 
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key,'user':user.data})

      
#################### هاذة الدالة نهائية عنستخدمها لتسجيل الدخول
@api_view(['POST'])

def Login(request):
        username = request.data.get("username")
        password = request.data.get("password")
       
        user = authenticate(username=username, password=password)
      
        if user:
            login(request, user)
           
            profile = CustomUser.objects.get(user=user)
            token, created = Token.objects.get_or_create(user=profile)
            return Response({
                "token": token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)
# @login_required 

@api_view(['POST'])
def login(request):
    user = request.user.id
    
    # Extract username and password from requestbody
    username = request.data.get('username')
    password = request.data.get('password')
    # userid=user.pk
    # Authenticate user
    user = authenticate(username=username, password=password)
    coustmer=CustomUser.objects.get(id=user) # type: ignore
    # If user is authenticated, create token and return it
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        print(username)
        return JsonResponse({'token': token.key,'user_id':coustmer.pk,'username':coustmer.username,'userphone':coustmer.PhonNumber})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)



class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])

def protected(request):
    # code to access protected resource
    return Response({'message': 'Welcome to the protected API!'})

#########################################333

@api_view(['POST'])
def create_account(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Account created successfully'})
    else:
        return Response(serializer.errors, status=400)





################################################################################
class UserLoginAPIView(APIView):
    # permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            messages.add_message(request, messages.SUCCESS, 'تم تسجيل الدخول بنجاح')
            return Response({'token': token.key})
        else:
          
            return Response({'فشل تسجيل الدخول'})






















#######################

class ProtectedView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
# class LoginAPI(APIView):
#     def post(self, request):
#         PhonNumber = request.data.get('PhonNumber')
#         password = request.data.get('password')

#         user = authenticate(request, PhonNumber=PhonNumber, password=password)
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             serializer = CustomUserSerializer(user)
#             return Response({
#                 'token': token.key,
#                 'user': serializer.data
#             })
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=401)

from django.contrib.auth.views import LoginView # type: ignore

# class CustomLoginView(LoginView):
#     template_name = 'login.html'



# class CustomUserLoginView(APIView):
#     def post(self, request):
#         serializer = CustomUserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response({'detail': 'Logged in successfully.'}, status=status.HTTP_200_OK)

# class LoginView(APIView):
#     permission_classes =[AllowAny]
#     # serializer_class = LoginSerializer
#     def post(self, request):
#         PhonNumber = request.data.get('PhonNumber')
#         password = request.data.get('password')
#         user = authenticate(request, username=PhonNumber, password=password)
#         if user is None:
#             token,created = Token.objects.get_or_create(user=user)
#             # تجديد فترة صلاحية التوكن في حال كانت فترة الصلاحية قد انتهت
#             if not token.is_valid():
#                 token.expired_at = timezone.now() + timedelta(days=7)
#                 token.save()
            
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

##########/////////////////////////////

class RefreshTokenView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = Token.objects.get(user=request.user)
        # تجديد فترة صلاحية التوكن
        token.expired_at = timezone.now() + timedelta(days=7) # type: ignore
        token.save()
        return Response({'token': token.key}, status=status.HTTP_200_OK)



################################################################


# class CustomTokenObtainPairView(TokenObtainPairView):
#     permission_classes = [AllowAny]

# class CustomTokenRefreshView(TokenRefreshView):
#     permission_classes = [AllowAny]



@login_required 
def dashboard(request):
        savaUser=request.user
        user_id=savaUser.id
        coust=CustomUser.objects.get(id=user_id)
        print('user id ='+ str(user_id))
        return render(request,'test.html', {'coust':coust})
def no_rest_from_model(request):
    data = CustomUser.objects.all()
    response = {
        'guests': list(data.values())
    }
    return JsonResponse(response)

def add_user(request):
    if request.user.is_authenticated:
        return render(request, 'add_coustmer.html')
  
@api_view(['GET','POST'])
def FBV_List(request):
    # GET
    if request.method == 'GET':
        coustm = CustomUser.objects.all()
        serializer = CoustSerializer(coustm, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = CoustSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

# @login_required



# class CustomAddView(View):
#     form_class = 

#     def form_valid(self, form):
#         remember_me = form.cleaned_data.get('remember_me')

#         if not remember_me:
#             # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
#             self.request.session.set_expiry(0)

#             # Set session as modified to force data updates/cookie to be saved.
#             self.request.session.modified = True

#         # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
#         return super(CustomLoginView, self).form_valid(form)




# class CBV_ListOfOrders(APIView):
#     def get(self, request):
#         coust = OrderDetiles.objects.all()
#         serializer = OrdersDetiSerializer(coust, many = True)
        
#         return Response(serializer.data)
#     def post(self, request,*args, **kwargs):
#         serializer = OrdersDetiSerializer(data= request.data)
#         print(serializer)
#         if serializer.is_valid():
        
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.data,
#             status= status.HTTP_400_BAD_REQUEST
#         )

class CBV_List(APIView):
    def get(self, request):
        coust = CustomUser.objects.all()
        serializer = CoustSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request,*args, **kwargs):
        serializer = CoustSerializer(data= request.data)
        print(serializer)
        if serializer.is_valid():
        
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

class CBVCatg_List(APIView):
    def get(self, request):
        savaUser=request.user
        user_id=savaUser.id
        print(user_id)
        coust = TypeAccount.objects.all()
        serializer = TypeCoustSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TypeCoustSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

class CBVCoustemSections_List(APIView):
    def get(self, request):
        coust = CoustemSections.objects.all()
        serializer = CoustemSectionSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CoustemSectionSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

class CBVProdects_List(APIView):
    def get(self, request):
        coust = Products.objects.all()
        serializer = ProdectSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProdectSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

@permission_classes([IsAuthenticated])
class UserRegistrationView(generics.CreateAPIView):
    """
    User registration view.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CoustSerializer

    def post(self, request, *args, **kwargs):
        """
        Post request to register a user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        coustmer = serializer.save()
        # token = Token.objects.create(coustmer)
        return Response(
            {
                "Coustmer": CoustSerializer(coustmer).data,
                # "token":token,
            },
            status=status.HTTP_201_CREATED,
       )
# class UserLoginAPIView(generics.GenericAPIView):
#     """
#     An endpoint to authenticate existing users using their email and password.
#     """

#     # permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer

#     def login(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = get_and_authenticate_user(**serializer.validated_data)
#         data = serializers.AuthUserSerializer(user).data
#         return Response(data=data, status=status.HTTP_200_OK)


# class LoginView(TokenObtainPairView):
#     """
#     Client login endpoint.
#     """

#     serializer_class = LoginSerializer


# 6 Generics 
#6.1 get and post
class generics_list(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CoustSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CoustSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

#7 viewsets
# class viewsets_guest(viewsets.ModelViewSet):
#     queryset = Guest.objects.all()
#     serializer_class = GuestSerializer

# class viewsets_movie(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     filter_backend = [filters.SearchFilter]
#     search_fields = ['movie']

# class viewsets_reservation(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = Reservation

# #8 Find movie
# @api_view(['GET'])
# def find_movie(request):
#     movies = Movie.objects.filter(
#         hall = request.data['hall'],
#         movie = request.data['movie'],
#     )
#     serializer = MovieSerializer(movies, many= True)
#     return Response(serializer.data)

# #9 create new reservation 
# @api_view(['POST'])
# def new_reservation(request):

#     movie = Movie.objects.get(
#         hall = request.data['hall'],
#         movie = request.data['movie'],
#     )
#     guest = Guest()
#     guest.name = request.data['name']
#     guest.mobile = request.data['mobile']
#     guest.save()

#     reservation = Reservation()
#     reservation.guest = guest
#     reservation.movie = movie
#     reservation.save()

#     return Response(status=status.HTTP_201_CREATED)


#10 post author editor
# class Post_pk(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# @unautheticated_user
# def loginPage(request):
    
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         user=authenticate(request,username=username,password=password)
#         if user != None: 
#             login(request, user)
#             user_type = Coustmer.TypeUser
#             print(user_type)
#             if user_type == '1':
#                 return redirect('dashboard')
                
#             elif user_type == '2':
#                 return redirect('dashboard')

#             elif user_type == '3':
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, "Invalid Login!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Invalid Login Credentials!")
#             return redirect('login')
    
#     return render(request,'login.html')
###################################
##هاذة الدالة تجلب الطلبات الخاصة ب المستخدم الي مسجل دخول
class GetUserOrderListByID(generics.ListAPIView):
    serializer_class = OrdersSerializer

    # def get_queryset(self):
    #     user_id = self.request.user.id
        
    #     return Order.objects.all()
###########################order_coustmerId=user_id


# def map_view(request):
#     return render(request, 'map.html', {'api_key': GOOGLE_MAPS_API_KEY})


# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrdersSerializer

# class OrderDetailCreateAPIView(generics.CreateAPIView):
#     queryset = OrderDetails.objects.all()
#     serializer_class = OrderDitilessiSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_view(request):
    content = {'message': 'Hello, World!'}
    return Response(content)

####################
# @api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
class CBV_Get_All_Orders_List(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        savaUser=request.user
        user_id=savaUser.id
        # coust = Order.objects.filter(order_coustmerId=user_id)
        coust = Order.objects.all()
        serializer = OrdersSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        savaUser=request.user
        user_id=savaUser.id
        print(user_id)
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )
# @authentication_classes([TokenAuthentication])

class CBV_Address_By_Id(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id=request.user.id
        print(user_id)
        coust = Address.objects.filter(address_coustem_id=user_id)
        serializer = AddressSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AddressSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
@permission_classes([IsAuthenticated])
class CBV_Address_List(APIView):
    def get(self, request):
        coust = Address.objects.all()
        serializer = AddressSerializer(coust, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AddressSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

################################
@permission_classes([IsAuthenticated])
class CBV_User_info_By_Id(APIView):
    def get(self, request):
        user_id=request.user.id
        print(user_id)
        coust = CustomUser.objects.filter(id=user_id)
        serializer = CoustSerializer(coust, many = True)
        return Response(serializer.data,)

from django.http import JsonResponse


@csrf_exempt   
def Search(request):
    
    data = json.load(request)
    search_text=data['name']
    print(data['name'])
    print('search_text'+search_text)
            # البحث في جدول المنتجات باستخدام النص المستلم من تطبيق Android
    products = Products.objects.filter(Q(namescient__icontains=search_text) | Q(namepasnes__icontains=search_text))

                # تحويل النتائج إلى قائمة من العناصر المتسلسلة
    results = []
    for product in products:
        coustmer=product.prodect_CoustmerId.pk
        vendor= CustomUser.objects.get(id=coustmer)
        image_url =product.photo.url
        data = {"image_url": image_url}
        json_data = json.dumps(data['image_url']) 
        result = {
                    'id': product.pk,
                    'namescient': product.namescient,
                    'namepasnes': product.namepasnes,
                    'quntity': product.quntity,
                    'desc': product.desc,
                    'vendor': vendor.username,
                    'price': product.price,
                    'photo': json_data,
                        # يمكنك إضافة المزيد من الحقول هنا
               }
        results.append(result)

                # إرجاع النتائج كـ JSON response
    return JsonResponse(results, safe=False)
 
    
#######################
# class CBV_Cart_List(APIView):
#     def get(self, request):
#         coust = Cart.objects.all()
#         serializer = CartSerializer(coust, many = True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = CartSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.data,
#             status= status.HTTP_400_BAD_REQUEST
#         )


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def save_location(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             latitude = data['latitude']
#             longitude = data['longitude']
#             location = Location(latitude=latitude, longitude=longitude)
#             location.save()
#             return JsonResponse({'message': 'Location saved successfully'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})








#################################################























####################
def logoutUser(request):
    logout(request)
    return redirect('login')
