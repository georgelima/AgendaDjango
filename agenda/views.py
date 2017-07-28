# encoding: utf8

from django.shortcuts import render, redirect, get_object_or_404
from agenda.models import ItemAgenda
from agenda.forms import FormItemAgenda

# Create your views here.

#
# Main page
#
def index(request):
    x = ItemAgenda.objects.all()
    return render(request,'lista.html',{ 'lista_itens': x } )

#
# Add new item in agenda
#
def adiciona(request):
    if request.method == 'POST':
        form = FormItemAgenda(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormItemAgenda()

    return render(request,'adiciona.html',{ 'form' : form })

#
# Edit agenda item
#
def edita_item(request,id):
    item = get_object_or_404(ItemAgenda,pk=id)
    form = FormItemAgenda(request.POST or None,instance=item)        
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'item.html',{ 'form':form })

#
# Remove agenda item
#
def remove_item(request,id):
    item = get_object_or_404(ItemAgenda,pk=id)
    item.delete()
    return redirect('/')








