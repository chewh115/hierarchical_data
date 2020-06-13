from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Files
from .forms import FilesForm

# Create your views here.
def index(request):
    context = {}
    context['files'] = Files.objects.all()
    return render(request, 'index.html', context)


def add_file(request):
    if request.method == "POST":
        form = FilesForm(request.POST)
        if form.is_valid():
            file_data = form.cleaned_data
            new_file = Files.objects.create(
                name = file_data['name'],
                parent = file_data['parent']
            )
            return HttpResponseRedirect(reverse('home'))
    form = FilesForm()
    return render(request, 'generic_form.html', {'form': form})