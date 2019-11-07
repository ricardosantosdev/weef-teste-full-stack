from .models import Class
from .forms import ClassForm
from django.shortcuts import render, redirect, get_object_or_404


def listening_classes(request):
    classes = Class.objects.all().order_by('-pk')
    return render(request, 'classes/classes.html', {'classes': classes})


def adding_classes(request):
    if request.method == 'POST':
        form_class = ClassForm(request.POST or None, auto_id=True)
        if form_class.is_valid():
            form_class.save()
        return redirect('classes')
    form_class = ClassForm()
    return render(request, 'classes/form.html', {'form_class': form_class})


def editing_classes(request, id):
    _class = get_object_or_404(Class, pk=id)
    form_class = ClassForm(request.POST or None, instance=_class)
    if form_class.is_valid():
        form_class.save()
        return redirect('classes')
    return render(request, 'classes/form.html', {'form_class': form_class})


def deleting_classes(request, id):
    pass
