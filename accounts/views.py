from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import CustomUser
from .forms import LoginForm, RegisterForm
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class LogoutView(auth_views.LogoutView):
    template_name= 'accounts/logout.html'

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class ProfileView(generic.DetailView):
    def get_object(self):
        print(self.request.user)
        return CustomUser.objects.get(username = self.request.user)
    
# def upload(request):
#     if request.method == 'POST':
#         print(request.method)
#         print(request.FILES['media'])
#         myfile = request.FILES['media']
#         print("---------------------------------")
#         print(myfile)
#         fs = FileSystemStorage(location='media/images/') #defaults to   MEDIA_ROOT 
#         print(fs)
#         filename = fs.save(myfile.name, myfile)
#         file_url = fs.url(filename)
#         return HttpResponse(fs)

#     return render(request, 'accounts/upload.html')

def upload(request):
    if request.method == 'POST':
        print("Entering Upload")
        # print(request.method)
        # print(request.FILES['media'])
        myfile = request.FILES['media']
        print("---------------------------------")
        print(myfile)
        path = 'media/images/'+myfile.name
        # fs = CustomUser.image(path, myfile().read())
        # file = request.FILES['media'].file.getvalue()
        # files = {'my_file': file}
        fs = FileSystemStorage(location='media/images/') #defaults to   MEDIA_ROOT 
        #print(fs)
        #filename = fs.save(myfile.name, myfile)
        #file_url = fs.url(filename)
        # print(myfile)
        return HttpResponse(path)

    return render(request, 'accounts/upload.html')