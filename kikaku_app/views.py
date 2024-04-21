from django.shortcuts import render, get_object_or_404
from .models import Project, Member, BlogPost

def home(request):
    projects = Project.objects.order_by('-date_posted')
    return render(request, 'home.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def blog(request):
    posts = BlogPost.objects.order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})

def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def contact(request):
    if request.method == 'POST':
        # フォームデータの処理
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # メール送信やデータ保存など（省略）
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')
