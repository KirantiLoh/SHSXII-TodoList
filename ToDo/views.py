from django.shortcuts import render, redirect
from .models import List, Item
from .forms import CreateItemForm, CreateToDoForm, SearchListForm

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def create_todo_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateToDoForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                list = List.objects.create(title = title, author = request.user)
                list.save()

                return redirect("Lists")
        else:
            form = CreateToDoForm        
        return render(request, "create_todo.html", {"form" : form})
    else:
        return redirect("login")

def lists_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SearchListForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title_search']
                lists = List.objects.filter(author =request.user, title__contains = title)
        else:
            form = SearchListForm
            lists = List.objects.filter(author = request.user)
        return render(request, "lists.html", {"lists" : lists, "form" : form})
    else:
        return redirect("login")

def list_view(request, id):
    if request.user.is_authenticated:
        list = List.objects.get(id=id)
        items = Item.objects.filter(list = list)

        if request.method == "POST":
            form = CreateItemForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data["content"]
                is_urgent = form.cleaned_data["is_urgent"]
                item = Item.objects.create(list = list, content = content, is_urgent = is_urgent)
                item.save()

                return redirect("List", id=id)
        else:
            form = CreateItemForm
        return render(request, "list.html", {"list" : list, "items" : items, "form" : form})
    else:
        return redirect("login")

def get_started(request):
    if request.user.is_authenticated:
        return redirect("Create")
    else:
        return redirect("register")

def delete_list(request, id):
    if request.user.is_authenticated:
        list = List.objects.get(id = id)
        list.delete()
        return redirect('Lists')
    else:
        return redirect('Home')

def delete_item(request, list_id, item_id):
    if request.user.is_authenticated:
        item = Item.objects.get(id = item_id)
        item.delete()
        return redirect('List', list_id)
    else:
        return redirect('Home')
