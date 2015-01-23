from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def index(request):
  all_posts = Post.objects.order_by('-pub_date')
  #Because it wouldn't all fit on one line.
  all_posts = all_posts.filter(pub_date__lte=timezone.now())
  context = {'all_posts': all_posts}
  return render(request, 'blog/index.html', context)

def detail(request, slug):
  context = {'selected_post': get_object_or_404(Post,slug=slug)}
  return render(request, 'blog/detail.html', context)
