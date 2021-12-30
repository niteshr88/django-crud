from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from StudentApp.models import Student, GetImage
# Create your views here.
def index(request):
    msg = False
    ErrorMsg = None

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        d_o_b = request.POST.get('d_o_b')
        address = request.POST.get('address')

        count = Student.objects.filter(email = email).count()
        if count > 0 :
            ErrorMsg = True
        else:
            std = Student(name=name, email=email, phone=phone, gender=gender, d_o_b=d_o_b, address=address)
            std.save()
    showmsg = {"msg": msg, "ErrorMsg":ErrorMsg}
    return render(request, 'index.html',showmsg)

def show(request):
    info = {}
    data = Student.objects.all()
    info = {'data': data}
    return render(request, 'edit.html', info)

def edit(request, email):
    data = Student.objects.get(email = email)
    send = {'data':data, 'gender':data.gender}
    return render(request, 'update.html', send)

def update(request):
    gender = None
    if request.method == "POST":
        email = request.POST.get("email")
        data = Student.objects.get(email=email)
        data.name = request.POST.get('name')
        data.phone = request.POST.get('phone')
        data.gender = request.POST.get('gender')
        # print("Gender: ", data.gender)
        data.d_o_b = request.POST.get('d_o_b')
        # print(data.d_o_b,"----------", data.gender)
        data.address = request.POST.get('address')
        data.save()
        return redirect('edit')
    else:
        return render(request,"edit.html")

def delete(request, email):
    data = Student.objects.get(email = email)
    data.delete()
    return redirect('edit')

def display(request):
    all_images = GetImage.objects.all()
    return render(request,'showImg.html', {"all_images":all_images})

def user(request):
    userCreationForm = UserCreationForm()

    return render(request,"user.html", {'usrCretionFrm':userCreationForm})