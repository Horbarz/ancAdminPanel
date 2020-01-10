from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from adminPost.forms import UpdateDoctorForm

from django.core.paginator import Paginator

# Create your views here.
from adminPost.forms import AddDoctorForm

from adminPost.forms import DoctorList

from adminPost.models import DoctorPost


def docAdd(request):
    form = AddDoctorForm(request.POST)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            post_saved = form.save(commit=False)
            post_saved.author = request.user.id
            form.save()
    return render(request, 'doctor_form.html', {'form': form })


def docList(request):
    form = DoctorList(request.POST)
    posts = DoctorPost.objects.all().order_by('-id').reverse()
    if request.method == 'POST':
        posts = DoctorPost.objects.filter.order_by('-id').reverse()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')

    posts = paginator.get_page(page)
    context_posts = {
        'posts':posts
    }
    return render(request,'all_doctors.html',context_posts)

def update_doc(request, pk):
    post = DoctorPost.objects.get(pk=pk)
    form = UpdateDoctorForm(request.POST,instance=post)

    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            form.save()
    # if request.is_ajax():
    #     template = 'doctor_update.html'
    # else:
    #     template= 'all_doctors.html'
    return render(request, 'doctor_update.html', {'form': form, 'post': post})

def delete_doc(request, pk):
	post = get_object_or_404(DoctorPost,pk=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('adminPost:doctorList')
	context = {
		"object": post
	}
	return render(request, 'delete.html', context)






