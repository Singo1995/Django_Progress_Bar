from rest_framework import generics,permissions
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.views import APIView 
from rest_framework.response import Response
from accounts.api.serializers import UserModelSerializer,UploadSerializer
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from rest_framework import serializers
import uuid

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    # form_one= BytesIO()
    # renderer_classes = [JSONRenderer]
    template_name = 'accounts/api_register.html'

    def get(self, request):
        serializer = UserModelSerializer()
        print("Reaching Get")
        # return Response({'serializer':serializer.data})
        return Response({'serializer': serializer})

    def post(self, request):
        # print(request.data)
        if request.data.get('image'):
            # print(request)
            print("Entering Upload Session")
            # print(form_one)
            # form_one = request.data.copy()
            # print(form_one)
            draft_request_data = request.data.copy()
            # draft_request_data.add('email')
            # print(uuid.uuid1)
            # draft_request_data['email'] = uuid.uuid1()
            # draft_request_data['username'] = "Arjunsinghania"
            #draft_request_data.pop('csrfmiddlewaretoken')
            # print(draft_request_data)
            #form_one = draft_request_data['media'].file
            #print(type(draft_request_data['media'].file))
            serializer = UploadSerializer(data = draft_request_data)
            print(serializer.is_valid())
            if serializer.is_valid():
                print("Reaching Validation")
                request.session['link_id'] = serializer.create(draft_request_data)

            return HttpResponse("Image Upload Successful")
            # print(serializer.is_valid())
            # if not serializer.is_valid():
            #     print(serializer.errors)
            # if serializer.is_valid():
            #     print(serializer.data)
            # request.session["uploadform"] = serializer.data
        #     print(request.session["uploadform"])
        #     # image = draft_request_data.get('image')
        #     # print(image)
        #     return HttpResponse("Image Upload Successful")
            # return messages.success(request, 'Image Upload Successful')
        # print(draft_request_data.image)
        # print("**********************")
        # print(type(draft_request_data))
        #print(draft_request_data)
        
        #draft_request_data.pop('confirm_password')
        # print(draft_request_data.get('image'))
        # path = 'media/images/'+ draft_request_data.get('image').name
        # draft_request_data['image'] = CustomUser.image(path, draft_request_data.get('image').read())
        if not request.data.get('image'):
            draft_request_data = request.data.copy()
            print("---------------------------------")
            # draft_request_data['image'] = form_one
            # file_handle = StringIO.StringIO(file.read())
            # image_file = InMemoryUploadedFile(buf,'file',"media/"+draft_request_data['image'],None,buff.tell(),None)
            # image_file = base64.b64encode(File(open("media/"+draft_request_data['image']), 'rb').read())
            # print(image_file)
            # draft_request_data['image'] = image_file
            # print(draft_request_data)
            serializer = self.get_serializer(data = draft_request_data)
            # serializer.image(path, draft_request_data.get('image').read())
            # print(serializer)
            # print(serializer.is_valid())
            
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'serializer': serializer})
            # print("serializer+++++++++++++++")
            # print(serializer.data.pop('confirm_password'))
            # print(serializer)
            print(request.session['link_id'])
            draft_request_data.pop('csrfmiddlewaretoken')
            serializer.create(draft_request_data,request.session['link_id'])
            return redirect('/login/')