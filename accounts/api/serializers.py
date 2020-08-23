from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()
link_id = 0

# class UploadSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(allow_null=True)
#     class Meta:
#         model = User
#         fields = ['image']

#         def create(self, validated_data):
#             print("Creating")
#             print(validated_data['image'])
#             print
#             fake = User.objects.create(image = validated_data['image'],email='',fullname='',dob='1995-11-06',phonenumber='',passportnumber='',username='',password='')
#             link_id = fake.id
#             print("link_id")
#             print(link_id)
#             return fake

class UploadSerializer(serializers.Serializer):
    image = serializers.ImageField(allow_null=True)

    def create(self, validated_data):
        print("Creating")
        print(validated_data['image'])
        print
        fake = User.objects.create(image = validated_data['image'],email=validated_data['image'].name,fullname='',dob='1995-11-06',phonenumber='',passportnumber='',username=validated_data['image'].name,password='')
        link_id = fake.id
        print("link_id")
        print(link_id)
        return link_id

class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ['email','fullname','dob','phonenumber','passportnumber','username','password','confirm_password']

    # def validate_image(self, image):
    #     print("Validating the Image")
    #     self.image = image
    #     img_handle = self.image.save()
    #     print(img_handle)
    #     return img_handle
    # def validate_email(self, email):
    #     existing = User.objects.filter(email=email).first()
    #     if existing:
    #         raise serializers.ValidationError("Someone with that email "
    #             "address has already registered. Was it you?")

    #     return email
    def validate(self, data):
        print("Entering Here")
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        
        if data.get('image'):
            print("Validating the Image")
            data['image'] = data['image'].save()
            print(data['image'])
        return data
    
    def create(self, validated_data, session_id):
        print("reaching here")
        print(session_id)
        # print(validated_data['image'])
        # if validated_data['image']:
        #     fake = User.objects.create(image = validated_data['image'],email='',fullname='',dob='1995-11-06',phonenumber='',passportnumber='',username='',password='')
        #     link_id = fake.id
        #     print("link_id")
        #     print(link_id)
        # if not validated_data['image']:
        print("Not Part")
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        print(validated_data)
        user = User.objects.get(id=session_id)
        user.email = validated_data['email']
        user.fullname = validated_data['fullname']
        user.dob = validated_data['dob']
        user.phonenumber = validated_data['phonenumber']
        user.passportnumber = validated_data['passportnumber']
        user.username = validated_data['username']
        user.password = validated_data['password']
        user.save()
        return user
            # return User.objects.create(**validated_data)
    # def create(self, validated_data):
    #     validated_data.pop('confirm_password')
    #     return User.objects.create(**validated_data)