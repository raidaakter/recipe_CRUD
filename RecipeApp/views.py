from django.shortcuts import redirect, render
from RecipeApp.models import *

# Create your views here.

def home(request):
    recipeData = recipeModel.objects.all()
    return render(request, 'home.html', {'recipes':recipeData})

def add_recipe(request):
    if request.method == 'POST':
        title= request.POST.get('title')
        description= request.POST.get('description')
        ingridient=request.POST.get('ingredients')
        instructions=request.POST.get('ingredients')
        image=request.FILES.get('image')
        print("i'm here")
        print("image: ", image)
        
        recipeData=recipeModel(
            Title=title,
            Description=description,
            Ingredients=ingridient,
            Instructions=instructions,
            Image=image,
        )
        recipeData.save()
        return redirect('home')
    return render(request, 'add_recipe.html')

def edit_recipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    if request.method == 'POST':
        recipeData.title= request.POST.get('title')
        recipeData.description= request.POST.get('description')
        recipeData.ingridient=request.POST.get('ingredients')
        recipeData.instructions=request.POST.get('ingredients')
        
        picture =request.FILES.get('Image')
        
        if picture is not None:
            recipeData.Image = picture
        recipeData.save()
        
        return redirect('home')
    
    return render(request, 'edit_recipe.html',{'recipe':recipeData})



def delete_recipe(request,id):
    recipe=recipeModel.objects.get(id=id).delete()
    return redirect('home')

def view_recipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    return render(request, 'view_recipe.html',{'recipe':recipeData})

