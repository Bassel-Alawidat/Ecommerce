from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template('food/index.html')
    context={
        'item_list':item_list,

    }
    #return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

class IndexClassView(ListView): #class based 
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'

def item(request):
    return HttpResponse('<h1>This is an item View</h1>')

def detail(request,item_id):
    item =Item.objects.get(pk=item_id)
    context= {
        'item':item,
    }
    return render(request,'food/detail.html',context)



class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'item_id'

   

#Add itemA""""" """"""
def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

#add item useing calss based
class CreatItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


#Update exsist item

def update_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

#Delete item
def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method =='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete-item.html',{'item':item})




