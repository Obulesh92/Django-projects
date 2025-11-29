from django.shortcuts import render,redirect
from .models import MyPhoto,MyVideo,Contact
# Create your views here.
 
def home(request):
    photo=MyPhoto.objects.all()
    return render(request,'index.html',{'allphoto':photo})

def add_post(request):
    if request.method=='POST':
        title=request.POST.get('title')
        image=request.FILES.get('image')
        date=request.POST.get('date')
        photo=MyPhoto(
            title=title,
            date=date,
            image=image if image else None
        )
        photo.save()
        return redirect('home')
    return render(request,'add_post',{'allphoto':photo})
def add_video(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        video=request.FILES.get('video')
        videos=MyVideo(
            title=title,
            description=description,
            video=video if video else None
        )
        videos.save()
        return redirect('video')
    return render(request,'add_video',{'allvideos':videos})



def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        comments=Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        comments.save()
        return redirect('contact')
    return render(request,'contact.html')
def video(request):
    video=MyVideo.objects.all()
    return render(request,'video_page.html',{'allvideo':video})
def about(request):
    return render(request,"about.html")