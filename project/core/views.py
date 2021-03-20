from django.shortcuts import render, redirect

from django.views.generic import ListView, TemplateView
from .forms import PostForm, PostSearchForm
from .models import Post
from .filters import PostFilter
from django.conf import settings

class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'
    filterset_class = PostFilter

    def get_queryset(self):
        qs = self.model.objects.filter().order_by('-id')
        filtered_list = PostFilter(self.request.GET, queryset=qs)
        return filtered_list.qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['filter_form'] = PostSearchForm(self.request.GET)
        context['base_url']=settings.BASE_URL
        return context

class UploadView(TemplateView):
    template_name = 'core/upload.html'

    def upload_image(request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm()
        return render(request, 'core/upload.html', {
            'form': form
        })
