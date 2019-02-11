from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteModelForm

# Create your views here.

def create_view(request):
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    context = {
        'form' : form
    }

    return render(request, 'notepad/create.html', context)

def list_view(request):
    notes = Note.objects.all()

    context = {
        'object_list' : notes
    }

    return render(request, "notepad/list.html", context)

def delete_view(request, id):
    item = Note.objects.filter(pk=id) # returns list
    if item.exists():
        item[0].delete()
    return redirect('list')

def update_view(request, id):
    unique_note = get_object_or_404(Note, pk=id)
    form = NoteModelForm(request.POST or None, request.FILES or None, instance=unique_note)
    if form.is_valid():
        form.save()
        return redirect('list')

    context = {
        'form' : form
    }

    return render(request, 'notepad/create.html', context)
