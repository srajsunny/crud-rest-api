from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import User
from django.views.generic import TemplateView, RedirectView, View

# Create your views here.
class UserAddShowView(TemplateView):
    template_name = 'crudapp/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=User.objects.all()
        context={'stu':stud, 'form':fm}
       
        return context 

    def post(self, request):
        fm=StudentRegistration(request.POST)
        print("hahhahaha mai hu kon")
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            print("haah",nm)
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            print("save ho gya h")
            return HttpResponseRedirect('/')
            

class UserDeleteData(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        pi=User.objects.get(pk=del_id)
        pi.delete()
        return super().get_redirect_url(*args, **kwargs)
         


class UpdateUserView(View):
    def get(self, request,id):
        print("edic click hua h",id)
        pi=User.objects.get(pk=id)  
        fm=StudentRegistration(instance=pi)
        return render(request, 'crudapp/updatestudent.html',{'form': fm})


    def post(self, request,id):
        print("update k post h",id)
        pi=User.objects.get(pk=id)
        

        fm=StudentRegistration(request.POST,instance=pi)
        
        if fm.is_valid():
            print("valid h")
            fm.save()
        return HttpResponseRedirect('/')    






       
        
    


