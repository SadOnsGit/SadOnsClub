from django.views.generic import TemplateView


class IndexPageTemplateView(TemplateView):
    template_name = 'club/index.html'


class AboutPageTemplateView(TemplateView):
    template_name = 'club/about.html'
