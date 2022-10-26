from django.shortcuts import render
#from django.http import HttpResponse

posts = [
	{
	'author':'Mone',
	'title':'Blog Post 1',
	'content':'First Post Content',
	'date_posted':'October 21, 2022'
	},
	{
	'author':'Jane Doe',
	'title':'Blog Post 2',
	'content':'Second Post Content',
	'date_posted':'October 25, 2022'
	}
]
# Create your views here.
def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog/home.html',context)


def about(request):
	return render(request,'blog/about.html',{'title':'About'})

 