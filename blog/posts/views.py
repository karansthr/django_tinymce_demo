from django.shortcuts import render ,get_object_or_404 , HttpResponseRedirect
from .models import Post
from .forms import postform

def post_list(request):
    post_set = Post.objects.all()
    return render(request,"post_list.html",{'posts':post_set})

def post_detail(request,id=None):
    article = get_object_or_404(Post , id = id)
    return render(request,"post_detail.html",{'instance':article})

def post_create(request):
    print("I was called")
    form = postform(request.POST or None )
    if form.is_valid():
        article = form.save(commit= False)
        article.save()
        return HttpResponseRedirect(article.get_absolute_url())
    return render(request, "post_form.html", {'form':form} )


def post_edit(request,id=None):
    article = get_object_or_404(Post , id = id)
    form = postform(request.POST or None, instance  = article )
    if form.is_valid():
        article = form.save(commit= False)
        article.save()
        return HttpResponseRedirect(article.get_absolute_url())
    return render(request, "post_form.html", {'form':form , 'instance':article} )
