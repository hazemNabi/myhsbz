from django.http import HttpResponse
from rest_framework import serializers
from .models import *
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from order.models import *
from prodect.models import *
from account.models import *
Coustmer = get_user_model()






from rest_framework import serializers
from django.contrib.auth import authenticate



from rest_framework import serializers
from django.contrib.auth.models import User
##1
class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # confirm_password = serializers.CharField(write_only=True)

    # def validate(self, data):
    #     if data.get('password') != data.get('confirm_password'):
    #        raise serializers.ValidationError("Passwords do not match")
    #     return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user( # type: ignore 
           username=validated_data.get('username'),
            password=validated_data.get('password'),
            TypeUser=validated_data.get('TypeUser'),
            PhonNumber=validated_data.get('PhonNumber'),
         
        )
        return user

    class Meta:
        model = CustomUser
        fields = ('id','username', 'password', 'TypeUser', 'PhonNumber')
        extra_kwargs = {
            'password': {'read_only': True},
        }











########################



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)

class CustomUserSerializer(serializers.ModelSerializer):
    # auth_token = TokenSerializer()

    class Meta:
        model =CustomUser
        fields = ('PhonNumber', 'passwoed')






# class CustomUserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = Coustmer
#         fields = ('PhonNumber', 'password')

#     def create(self, validated_data):
#         user = Coustmer.objects.create_user(
#             PhonNumber=validated_data['PhonNumber'],
#             password=validated_data['password']
#         )
#         return user

class LoginSerializer(serializers.Serializer):
    PhonNumber = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        PhonNumber = data.get('PhonNumber', None)
        password = data.get('password', None)

        if PhonNumber is None:
            raise serializers.ValidationError('An PhonNumber  is required to log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(email=PhonNumber, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid PhonNumber/password combination.')

#         if not user.is_active:
#             raise serializers.ValidationError('This user has been deactivated.')
        
#         return {'user': user}



























###########################################
class TypeCoustSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields ='__all__'


class CoustSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'
        # ("username", "PhonNumber", "TypeUser", "password")
    

    def create(self, validated_data, **kwargs):
        """
        Overriding the default create method of the Model serializer.
        """
        print(validated_data)
        coustmer = CustomUser(
            username=validated_data["username"],
            TypeUser=validated_data["TypeUser"],
            PhonNumber=validated_data["PhonNumber"],
        )
        password = validated_data["password"]
        coustmer.set_password(password)
        coustmer.save()
        return coustmer

# class UserLoginSerializer(serializers.Serializer):
#     """
#     Serializer class to authenticate users with email and password.
#     """
#     # username = None
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
 



# class AuthUserSerializer(serializers.ModelSerializer):
#     auth_token = serializers.SerializerMethodField()

#     class Meta:
#          model = User
#          fields = ('PhonNumber', 'password')
         
    
#     def get_auth_token(self, obj):
#         token = Token.objects.create(user=obj)
#         return token.key


# class LoginSerializer(TokenObtainPairSerializer):
#     PhonNumber = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     class Meta:
#           model = Coustmer
#         #   fields = '__all__'
#     def validate(self, attrs):
       
#         data = super(LoginSerializer, self).validate(attrs)
     
#         data.update()
#         token = Token.objects.get(user=self.user)
        
#         respons={
#             'data':data,
#             'token':token.key,
#             'msg':'Login Succsful'
#         }
       
#         return respons 

class CoustemSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoustemSections
        fields ='__all__'


# class OhdatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ohdat
#         fields ='__all__'

# class MyPriceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyPrice
#         fields ='__all__'

class ProdectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields ='__all__'
        
# class OrdersDetiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetiles
#         fields ='__all__'


class OrderDitilessiSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = OrderDetails
        fields ='__all__'
   

class OrdersSerializer(serializers.ModelSerializer):
    # items = serializers.CharField(source='items')
    items=OrderDitilessiSerializer(many=True,read_only=False)
    class Meta:
        model = Order
        fields ='__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetails.objects.create(**detail_data)
        return order


# from django.views.decorators.csrf import csrf_exempt

# from django.http import JsonResponse
# @csrf_exempt
# def create_or_update_order(request):
#     if request.method == 'POST':
#         # استخراج البيانات من الطلب الوارد
#         customer_name = request.POST.get('order_coustmerId')
       
#         delivery_address = request.POST.get('delivery_address')
#         order_id = request.POST.get('order_id')
        
#         # إنشاء طلب جديد أو تحديثه إذا وجد
#         if order_id:
#             order = Order.objects.filter(id=order_id).first()
#             if order:
#                 order.order_coustmerId = customer_name
              
#                 order.delivery_address = delivery_address
#                 order.save()
#                 return JsonResponse({'status': 'success', 'message': 'Order updated successfully'})
#             else:
#                 return JsonResponse({'status': 'error', 'message': 'Order not found'})
#         else:
#             order = Order.objects.create(
#                 customer_name=customer_name,
               
#                 delivery_address=delivery_address
#             )
#             return JsonResponse({'status': 'success', 'message': 'Order created successfully'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



    # def create(self, validated_data):
    #     # Extract nested data
    #     # customer_data = validated_data.pop('customer')
    #     items_data = validated_data.pop('items')

        # Create customer object
        # customer_serializer = CustomUserSerializer(data=customer_data)
        # customer_serializer.is_valid(raise_exception=True)
        # customer = customer_serializer.save()

        # Create order object
        # order = Order.objects.create(customer=customer, **validated_data)

        # Create order item objects
        # for item_data in items_data:
        #     item_data['order'] = order.pk
        #     item_serializer = OrderDitilessiSerializer(data=item_data)
        #     item_serializer.is_valid(raise_exception=True)
        #     item_serializer.save()

        # return order
# class OrdersSerializer(serializers.ModelSerializer):
#     items=OrderDitilessiSerializer(many=True,read_only=False)
#     class Meta:
#         model = Order
#         fields ='__all__'

    # def create(self, validated_data):
    #     print("ssssssssssssssss")
    #     details_data = validated_data.pop('items')
    #     print("order detiles 1111 :          ${details_data}")
    #     order = Order.objects.create(**validated_data)
    #     print("order detiles 2222 :          ${order}")
    #     for detail_data in details_data:
    #       s= OrderDetails.objects.create(order=order, **detail_data)
    #       print("order detiles 3333:          ${s}")
    #     return order
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields ='__all__'


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields ='__all__'


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = CustomUser
    fields = ['username', 'password']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields ='__all__'         # ('id', 'username', 'email','TypeUser','PhonNumber')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coustmer
#         fields = ('username', 'PhonNumber', 'password')
        

#     def create(self, validated_data):
#         user = Coustmer.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user


##############
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email",)
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password.', code='authorization')
        else:
            raise serializers.ValidationError('Email and password are required.', code='authorization')
        attrs['user'] = user
        return attrs
# class UserChangePassowrdSerializer(serializers.Serializer):
    # passowrd=serializers.CharField(max_length=255,write_only=True)
    # passowrd2=serializers.CharField(max_length=255,write_only=True)
    # class Meta:
    #     fields=['passowrd','passowrd2']
    # def validate(self, attrs):
    #      passowrd=attrs.get('passowrd')
    #      passowrd2=attrs.get('passowrd2')
    #      user=self.context.get('user')
    #      if passowrd != passowrd2:
    #         raise serializers.ValidationError('Passowrd and Confirm Passowrd dosent match')
    #      user.set_password(passowrd)
    #      user.save()
    #      return attrs