from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is a home page")
    context={'name':'Susmita Shiwakoti', 'course':'Django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is a about page")
    return render(request, 'about.html')

def project(request):
    # return HttpResponse("This is project page")
    return render(request, 'project.html')

def contact(request):
    # return HttpResponse("This is contact page")
    return  render(request, 'contact.html')


def student(request):
    a=100
    b=200
    c= int(a) + int(b)
    return HttpResponse("Summation of a and b is ", c)

