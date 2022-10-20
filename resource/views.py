from django.shortcuts import render
from django.http import HttpResponse

def names(request):
    return HttpResponse('This is Names List')

def list(request, pk):
    firstnames = "abebe"
    return HttpResponse(firstnames)


# testing a list renderer
def add_student(request):
    if request.method == 'POST':
        student_list = []
        student_name = request.POST.getlist('student_name')
        student_phone = request.POST.getlist('student_phone')

        zipped = zip(student_name,student_phone)

        for student_name,student_phone in zipped:
            student = Student.objects.create(student_name=student_name,
                                             student_phone=student_phone)
            student_list.append(student)

        return render(request,'students/view_all_student.html', {'instances': student_list})
    else:
        return render(request,'students/add_student.html')

