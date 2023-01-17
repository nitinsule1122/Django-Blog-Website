from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blog
from django_update_from_dict import update_from_dict

# Create your views here.


def home(request):
	if request.method == "POST":		
		Title = request.POST.get('title')		
		Content = request.POST.get('content')
		Short_Desc = request.POST.get('short_desc')
		Slug = request.POST.get('slug')
		Blog.objects.create(title=Title,  content=Content, short_desc=Short_Desc, slug=Slug)
		return redirect('/')

	return render(request, 'index.html')



def blog(request):
	blogs = Blog.objects.all()
	context = {'blogs':blogs}
	return render(request, 'bloghome.html', context)

def blogpost(request, slug):
	blog = Blog.objects.filter(slug = slug ).first()
	context = {'blog':blog}
	return render(request, 'blogpost.html', context)

def addblog(request):
	if request.method == "POST":		
		Title = request.POST.get('title')		
		Content = request.POST.get('content')
		Short_Desc = request.POST.get('short_desc')
		Slug = request.POST.get('slug')
		Blog.objects.create(title=Title,  content=Content, short_desc=Short_Desc, slug=Slug)
		return redirect('/bloghome')

	return render(request, 'addblog.html')

def editblog(request,sno):
	Current_Object = Blog.objects.get(sno=sno)
	if request.method == "POST":
		Sno = request.POST.get('sno')
		Title = request.POST.get('title')
		Content = request.POST.get('content')
		Short_Desc = request.POST.get('short_desc')
		Slug = request.POST.get('slug')
		update_from_dict(Current_Object, dict(sno=Sno, title=Title,  content=Content, short_desc=Short_Desc, slug=Slug), commit=True)

		return redirect('/bloghome')


	return render(request, 'editblog.html', {'Current_Object':Current_Object})

def delete_data(request,sno):
	data = Blog.objects.get(sno=sno)
	data.delete()
	return redirect('/bloghome')



def search(request):
	return render(request, 'search.html')

def contact(request):
	return render(request, 'contact.html')
