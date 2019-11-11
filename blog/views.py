from django.shortcuts import render, get_object_or_404
from django.http import Http404


#from .mocks import Post
from .models import Post

#posts= [

	#{'id': 1, 'title': 'First Post', 'body': 'This is my first post'},
	#{'id': 2, 'title': 'Second Post', 'body': 'This is my second post'},
	#{'id': 3, 'title': 'Third Post', 'body': 'This is my this post'},
#]


# Create your views here.



def index(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts': posts})


def show(request,id):
	post = get_object_or_404(Post, pk=id)
	#try:
		#post = Post.objects.get(pk=id)
	#except Post.DoesNotExist:
		#raise Http404('Sorry the post #{} was not found.' .format(id))

	return render(request, 'blog/show.html', {'post': post})

