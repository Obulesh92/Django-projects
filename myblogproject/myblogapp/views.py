from django.shortcuts import render,redirect
from .models import myblog,contact
from django.contrib import messages
# Create your views here.
def display(request):
    blogs=myblog.objects.all()
    return render(request,'index.html',{"allblogs":blogs})
def add_blog(request):
    if request.method=="POST":
        post_title=request.POST.get('post_title')
        your_name=request.POST.get('your_name')
        Category=request.POST.get('Category')
        image_link=request.POST.get('image_link')
        Content=request.POST.get('Content')
        Tags=request.POST.get('Tags')
        blogs=myblog(
            post_title=post_title,
            your_name=your_name,
            Category=Category,
            image_link=image_link if image_link else None,
            Content=Content,
            Tags=Tags 
        )
        blogs.save()
        return redirect('allblogs')
    return render(request,'addblog',{"allblogs":blogs})


def full_blog(request,id):
    blogs=myblog.objects.filter(id=id)
    return render(request,'blog.html',{"allblogs":blogs})

def contact_data(request):
    if request.method == "POST":
        name = request.POST.get('your_name')
        your_email = request.POST.get('your_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Optional: basic validation
        if name and your_email and message:
            contact_entry = contact(  # Use your actual model name (usually starts with capital)
                your_name=name,
                your_email=your_email,
                subject=subject,
                message=message
            )
            contact_entry.save()
            return redirect('contact')  # Prevents resubmission on refresh
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contact.html')