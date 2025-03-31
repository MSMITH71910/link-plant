from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# INTERNAL
# list out the links 
# create a new link

# EXTERNAL
# see a profile (and its links)

class LinkListView(ListView):
    model = Link
    # def template model_list.html

class LinkCreateView(CreateView):
    model = Link
    # template - model_form.html
    # figure out what fields - could pass a list
    fields = "__all__"
    # success_url
    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):  # Fixed indentation
    model = Link
    template_name = 'link_plant/link_form.html'
    fields = ['text', 'url', 'profile']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):  # Fixed indentation
    model = Link
    template_name = 'link_plant/link_confirm_delete.html'
    success_url = reverse_lazy('link-list')

# External profile view - could be a ListView or a function view
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    return render(request, 'link_plant/profile.html', context)