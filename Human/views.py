from pydoc import pager
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from unicodedata import category


# Create your views here.
from .models import Humans, Category
from .forms import HumansForm, UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Регистрация прошла успешно')
           user = form.save()
           login(request, user)
       else:
           messages.error(request, 'Ошибка регистрации')
    else:
       form = UserRegisterForm()
    return render(request, 'Human/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
       form = UserLoginForm(data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request, user)
           return redirect('Home')
    else:
       form = UserLoginForm()
    return render(request, 'Human/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')





class HomeHumans(ListView, MyMixin):
    model = Humans
    context_object_name = 'humans'
    template_name = 'Human/home_humans_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Главная страница'
        return context

    def get_queryset(self):
        return Humans.objects.filter(is_published=True).select_related('category')


class HumansByCategory(ListView, MyMixin):
    model = Humans
    template_name = 'Human/home_humans_list.html'
    context_object_name = 'humans'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Humans.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewHumans(DetailView):
    model = Humans
    context_object_name = 'humans_item'

class AddHumans(CreateView):
    form_class = HumansForm
    template_name = 'Human/add_human.html'
    login_url = '/admin/'



# def test(request):
#    objects = ['Ahmed', 'Maga', 'Iba', 'Ahmed2', 'Maga2', 'Iba2']
#    paginator = Paginator(objects, 2)
#    page_num = request.GET.get('page', 1)
#    page_objects = paginator.get_page(page_num)
#    return render(request, 'Human/test.html', {'page_obj': page_objects})



# def index(request):
#   humans = Humans.objects.all()
#   categories = Category.objects.all()
#   context = {
#       'humans': humans,
#       'title': 'Список людей',
#   }
#   return render(request, 'Human/index.html', context = context)



# def get_category(request, category_id):
#    humans = Humans.objects.filter(category_id=category_id)
#    categories = Category.objects.all()
#    category = Category.objects.get(pk=category_id)
#    context = {
#        'humans': humans,
#        'category': category
#    }
#    return render(request, 'Human/category.html', context=context)



# def view_human(request, human_id):
#    #human_item = Humans.objects.get(pk=human_id)
#    humans_item = get_object_or_404(Humans, pk=human_id)
#    context = {
#        'human_item': humans_item
#    }
#    return render(request, 'Human/view_human.html', context=context)




# def add_human(request):
#    if request.method == 'POST':
#        form = HumansForm(request.POST)
#        if form.is_valid():
#           # humans = Humans.objects.create(**form.cleaned_data)
#            humans = form.save()
#            return redirect(humans)
#    else:
#         form = HumansForm()
#    return render(request, 'Human/add_human.html', {'form': form})









