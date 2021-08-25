import posts
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        print(request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    # 
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}

    return render(request, 'post.html', context)


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    # print(post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            # print("hello w")
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())
    else:
        form = PostForm
    # context = {'posts':Post.objects.all()}
        return render(request, 'edit.html', {'posts': post, 'form': form})


def like(request, post_id):
    post = Post.objects.get(id=post_id)

    post.like_count += 1

    post.save()

    return HttpResponseRedirect("/")
