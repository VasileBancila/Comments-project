from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from .forms import CommentsForm

def home(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = CommentsForm()
            comments = Comments.objects.all()
            context = {'form': form, 'comments': comments}
            return render(request, 'comments/home.html', context)
    else:
        form = CommentsForm()
        comments = Comments.objects.all()
        context = {'form': form, 'comments': comments}
        return render(request, 'comments/home.html', context)

def whole(request, id):
    try:
        comment = Comments.objects.get(pk=id)
    except Comments.DoesNotExist:
        comment = None

    context = {'comment': comment}
    return render(request, 'comments/whole.html', context)