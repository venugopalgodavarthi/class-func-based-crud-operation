from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from cbv.forms import fbvform, ucbvform, pcbvform
from cbv.models import pcbvmodel, fbvmodel, ucbvmodel
# Create your views here.

# userdefined function view
def fbvview(request, pk):
    res = fbvmodel.objects.get(id=pk)
    if request.method == 'POST':
        res = fbvmodel.objects.get(id=pk).delete()
        return HttpResponse("data deleted")
    return render(request, 'fbv.html', {'form': res})

# userdefined class view
class ucbvview(View):
    def get(self, request, pk):
        res = ucbvmodel.objects.get(id=pk)
        return render(request, 'ucbv.html', {'form': res})

    def post(self, request, pk):
        res = ucbvmodel.objects.get(id=pk).delete()
        return HttpResponse("data is deleted")
# perdefined class view (form view)


class pcbvview(DeleteView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    context_object_name = 'form'
    success_url = "/success/"


def success(request):
    return HttpResponse("data is deleted")


'''
# userdefined function view


def fbvview(request):
    return HttpResponse("haii function based view")

# userdefined class view


class ucbvview(View):
    def get(self, request):
        return HttpResponse("haii class based view")


# perdefined class view


# userdefined function view


def fbvview(request):
    return render(request, 'fbv.html')

# userdefined class view


class ucbvview(View):
    def get(self, request):
        return render(request, 'ucbv.html')

# perdefined class view


class pcbvview(TemplateView):
    template_name = 'pcbv.html'




# userdefined function view


def fbvview(request, data):
    return render(request, 'fbv.html', {'data': data})

# userdefined class view


class ucbvview(View):
    def get(self, request, data):
        return render(request, 'ucbv.html', {'data': data})

# perdefined class view


class pcbvview(TemplateView):
    template_name = 'pcbv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = 'Qspiders'
        return context

# userdefined function view


def fbvview(request):
    form = fbvform()
    return render(request, 'fbv.html', {'form': form})

# userdefined class view


class ucbvview(View):
    def get(self, request):
        form = ucbvform()
        return render(request, 'ucbv.html', {'form': form})

# perdefined class view


class pcbvview(FormView):
    template_name = 'pcbv.html'
    form_class = pcbvform




# userdefined function view


def fbvview(request):
    form = fbvform()
    if request.method == 'POST':
        form = fbvform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form data ")
    return render(request, 'fbv.html', {'form': form})

# userdefined class view


class ucbvview(View):
    def get(self, request):
        form = ucbvform()
        return render(request, 'ucbv.html', {'form': form})

    def post(self, request):
        form = ucbvform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form data")
        return render(request, 'ucbv.html', {'form': form})

# perdefined class view (form view)


class pcbvview(FormView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    form_class = pcbvform
    success_url = "/cbv/"

    def form_valid(self, form):
        user = super().form_valid(form)
        form.save()
        return user

# userdefined function view


def fbvview(request):
    form = fbvform()
    if request.method == 'POST':
        form = fbvform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form data ")
    return render(request, 'fbv.html', {'form': form})

# userdefined class view


class ucbvview(View):
    def get(self, request):
        form = ucbvform()
        return render(request, 'ucbv.html', {'form': form})

    def post(self, request):
        form = ucbvform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form data")
        return render(request, 'ucbv.html', {'form': form})


# perdefined class view (form view)


class pcbvview(FormView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    form_class = pcbvform
    success_url = "/cbv/"

    def form_valid(self, form):
        user = super().form_valid(form)
        form.save()
        return user


# perdefined class view (form view)


class pcbvview(CreateView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    form_class = pcbvform
    success_url = "/cbv/"



# userdefined function view


def fbvview(request):
    res = fbvmodel.objects.all()
    return render(request, 'fbv.html', {'res': res})

# userdefined class view


class ucbvview(View):
    def get(self, request):
        res = ucbvmodel.objects.all()
        return render(request, 'ucbv.html', {'res': res})

# perdefined class view

class pcbvview(ListView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    context_object_name = 'res'

# userdefined function view


def fbvview(request,pk):
    res = fbvmodel.objects.get(id=pk)
    return render(request, 'fbv.html', {'res': res})

# userdefined class view


class ucbvview(View):
    def get(self, request,pk):
        res = ucbvmodel.objects.get(id=pk)
        return render(request, 'ucbv.html', {'res': res})

# perdefined class view

class pcbvview(DetailView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    context_object_name = 'res'

# userdefined function view
def fbvview(request, pk):
    res = fbvmodel.objects.get(id=pk)
    form = fbvform(instance=res)
    if request.method == 'POST':
        form = fbvform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return HttpResponse("form data")
    return render(request, 'fbv.html', {'form': form})

# userdefined class view
class ucbvview(View):
    def get(self, request, pk):
        res = ucbvmodel.objects.get(id=pk)
        form = ucbvform(instance=res)
        return render(request, 'ucbv.html', {'form': form})

    def post(self, request, pk):
        res = ucbvmodel.objects.get(id=pk)
        form = ucbvform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return HttpResponse("form data")
        return render(request, 'ucbv.html', {'form': form})

# perdefined class view (form view)
class pcbvview(UpdateView):
    template_name = 'pcbv.html'
    model = pcbvmodel
    form_class = pcbvform
    success_url = "/success/"


def success(request):
    return HttpResponse("data is stored")



'''
