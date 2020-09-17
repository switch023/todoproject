from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import TodoModel
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

def topfunc(request):
  return render(request, 'toppage.html', {'some':100})

def signupfunc(request):
  if request.method == 'POST':
      entryname = request.POST['username']
      entrypassword = request.POST['password']
      try:
        User.objects.get(username = entryname)
        return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
      except:
        user = User.objects.create_user(entryname, '', entrypassword)
        return render(request, 'signup.html')
  return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
      entryname = request.POST['username']
      entrypassword = request.POST['password']
      user = authenticate(request, username = entryname, password = entrypassword)
      if user is not None:
        login(request, user)
        return redirect('list')
      else:
        return redirect('login')
    return render(request, 'login.html')

def logoutfunc(request):
  logout(request)
  return redirect('top')

@login_required
def listfunc(request):
  object_list = TodoModel.objects.all()
  return render(request, 'list.html', {'object_list':object_list})

def detailfunc(request, pk):
  object = TodoModel.objects.get(pk = pk)
  return render(request, 'detail.html', {'object': object})

class TodoCreate(CreateView):
  template_name = 'create.html'
  model = TodoModel
  fields = ('title', 'content', 'priority', 'duedate')
  success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
  template_name = 'delete.html'
  model = TodoModel
  success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
  template_name = 'update.html'
  model = TodoModel
  fields = ('title', 'content', 'priority', 'duedate')
  success_url = reverse_lazy('list')