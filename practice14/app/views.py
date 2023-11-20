from django.shortcuts import render, redirect, get_object_or_404
from app.form import PostForm
from app.models import Post




def all_posts_view(request):
    posts = Post.objects.all()
    context = {'post_list': posts}
    return render(request,
                  'all_posts_page.html',context)


def create_post_view(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author_post = form.cleaned_data['author_post']
            title_post = form.cleaned_data['title_post']
            text_post = form.cleaned_data['text_post']
            likes_post = form.cleaned_data['likes_post']
            

            post = Post()
            post.author_post = author_post
            post.title_post = title_post
            post.text_post = text_post
            post.likes_post = likes_post
            post.save()
            return redirect('all_posts_url')
    
    form = PostForm()
    context['form'] = form

    return render(request,
                  'create_post_page.html',context)



def post_page_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    

    return render(request,
                  'post_page.html',context)




