from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Subject, pastPaper, Slide, Video, Announcement
from django.contrib.auth.models import User
from django.http.response import JsonResponse
import pyotp
# Create your views here.


def index(request):

    if request.method == "GET":
        template_url = "web/index.html"
        return render(request, template_url)


@login_required(login_url="/")
def dashboard(request):

    if request.method == "GET":
        template_url = "web/dashboard.html"
        return render(request, template_url)

    if request.method == "POST" and request.POST['type'] == 'getPapers':
        papers = pastPaper.objects.all()
        past_papers = []
        
        for i in papers:
            data = {"subject": i.subject.subject_name, "date": i.Description, "file": str(i._file)}
            past_papers.append(data)

        return JsonResponse({"data": past_papers})


@login_required(login_url="/login")
def slides(request):

    if request.method == "GET":
        template_url = "web/slides.html"
        return render(request, template_url)

    if request.method == "POST" and request.POST['type'] == 'getSlides':
        papers = Slide.objects.all()
        slides = []
        
        for i in papers:
            data = {"subject": i.subject.subject_name, "date": i.Description, "file": str(i._file)}
            slides.append(data)

        return JsonResponse({"data": slides})

@login_required(login_url="/login")
def videos(request):

    if request.method == "GET":
        template_url = "web/Videos.html"
        return render(request, template_url)

    if request.method == "POST" and request.POST['type'] == 'getVideos':
        videos = Video.objects.all()
        array = []
        
        for i in videos:
            data = {"subject": i.subject.subject_name, "description": i.Description, "link": i.link}
            array.append(data)

        return JsonResponse({"data": array})

@login_required(login_url="/login")
def announcements(request):

    if request.method == "GET":
        template_url = "web/annoncements.html"
        return render(request, template_url)

    if request.method == "POST" and request.POST['type'] == 'getAnnouncements':
        announcements = Announcement.objects.all()
        array = []
        
        for i in announcements:
            data = {"announcement": i.announcement, "date":str(i.date.day)+"-"+str(i.date.month)+"-"+str(i.date.year)}
            array.append(data)

        return JsonResponse({"data": array})



def registration(request):
    if request.method == "POST" and request.POST["type"] == "createUser":
        userName = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        Message = "Successful"
        print(userName, email, firstName)
        ##check if user exists 
        userExists = User.objects.filter(username=userName).exists()
        emailExists = User.objects.filter(email=email).exists()
        passwordLength = len(password)
        if userExists == False and passwordLength >= 8 and userName not in password and emailExists == False:
            try:
                passwordIsInt = int(password)
                Message = "Your password is entirely numeric"
            except:
                ##create new user instance
                new_user = User()
                new_user.username = userName
                new_user.email = email
                new_user.set_password(password)
                new_user.first_name = firstName
                new_user.last_name = lastName
                new_user.save()
                
                
        else:
            if userExists == True:
                Message = "Error: the username is already in use."
            elif passwordLength < 8:
                Message = "Error: Password must be atleast 8 charcters long"
            elif userName in password:
                Message = "Error: You password is too similar to your mobile number"
            elif emailExists == True:
                Message = "Error: Please correct email address" 
        
        
        return JsonResponse({"Message":Message})
