from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    form =StudentRegistration()
    stud = User.objects.all()
    return render(request,'home.html',{'form':form, 'stu':stud})

@csrf_exempt
def save_data(request):
    if request.method =="POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            city = request.POST['city']
            if(sid == ''):
                usr = User(name= name,email= email, city= city)
            else:
                usr = User(id=sid, name= name,email= email, city= city)
            usr.save()
            stud = User.objects.values()
            #print(stud)
            student_data = list(stud)
            return JsonResponse({'status':'Save','student_data':student_data})
        else:
            return JsonResponse({'status':0})

#delete data
def delete_data(request):
    if request.method =="POST":
        id =request.POST.get('sid')
        #print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

#edit data
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(pk=id)
        student_data = {"id":student.id, "name":student.name, "email":student.email,
        "city":student.city}
        return JsonResponse(student_data)
