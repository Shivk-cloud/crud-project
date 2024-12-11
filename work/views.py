from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .form import AddStudentform
from django.contrib import messages

# Create your views here.
class Home(View):
    def get(self, request):
        stu_data=Student.objects.all()
        return render(request, 'work/home.html',{'studata':stu_data})

class Add_Student(View):
    def get(self, request):
        fm=AddStudentform
        return render(request, 'work/add-student.html', {'form':fm})
        
    def post(self, request):
         fm=AddStudentform(request.POST)
         if fm.is_valid():
             fm.save()
             return redirect("/")
         else:
            return render(request, 'work/add-student.html', {'form':fm})

class Delete_Student(View):
    def post(self, request):
        data=request.POST
        id=data.get('id')
        studata=Student.objects.get(id=id)
        studata.delete()
        messages.success(request, 'Object deleted successfully!')
        return redirect("/")


class Edit_Student(View):
    def get(self, request, id):
        stu=Student.objects.get(id=id)
        fm=AddStudentform(instance=stu)
        return render(request, 'work/edit-student.html',{'form':fm})

    

    def post(self, request, id):
        stu=Student.objects.get(id=id)
        fm=AddStudentform(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect("/") 
        else:
            return render(request, 'work/edit-student.html',{'form':fm})
        


