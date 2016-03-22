from django.shortcuts import render
from django.utils import timezone
from .models import Item
from .forms import ItemForm
from django.http import HttpResponseRedirect


def post_list(request):
    posts = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'catcolony/post_list.html', {'posts': posts})

def cutetag(request):
    posts = Item.objects.filter(tags=['cute'])
    return render(request, 'catcolony/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = ItemForm()
    return render(request, 'catcolony/post_edit.html', {'form': form})
