from django.db.models import Q #allows for searches in multiple fields.
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render, get_object_or_404

from .models import Post,Category
from .forms import CommentForm

# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    
    # to verify the input of the comment and save it only if it's valid
    if request.method == 'POST':  #checks if it's a post request which means data has been sent
        form= CommentForm(request.POST) #request.Post gets the data from the post command and sends it to the (comment object)form
        if form.is_valid():
            comment = form.save(commit=False)  # the comment form cannot save without pionting to the foreignkey which is the post(else crash), hence we save the form in a comment object
            comment.post=post  #get the post that is related to the comment and assign it to the foreignkey,else it will throw an error as the [post] attribute is a foreign key and must be known to properly link the comment
            comment.save()  #now save the comment object as all the fields are complete
            
            return redirect('post_detail',slug=slug)
    else:
        form = CommentForm()
                
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post':post, 'form':form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug,)
    posts = category.posts.filter(status=Post.ACTIVE)
    
    return render(request, 'blog/category.html', {'category':category, 'posts':posts})

def search(request):
    query = request.GET.get('query','') #used to get parameters of the search feature
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains= query) | Q(body__icontains= query)) #the icontains, negates the lowercase searching
    
    return render(request, 'blog/search.html', {'posts': posts, 'query':query})