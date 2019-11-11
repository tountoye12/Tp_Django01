from django.http import Http404

class Post(object):
	POSTS = [
	{'id': 1, 'title': 'First Post', 'body': 'This is my first post'},
	{'id': 2, 'title': 'Second Post', 'body': 'This is my second post'},
	{'id': 3, 'title': 'Third Post', 'body': 'This is my this post'},
	]

	
	@classmethod    
	def all(cls):
		return cls.POSTS

    
	@classmethod
	def find(cls, id):
		try:
			return cls.POSTS[int(id) - 1]
		except:
			raise Http404('pardon, Post #{} not found'.format(id))



 
		