import email
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from product.models import CategoryModel, ProductModel

# Create your views here.

class FrontPageView(TemplateView):
        template_name = 'general/front_page.html'

class HomeView(TemplateView):
    template_name = 'general/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = ProductModel.objects.all()
        categories = CategoryModel.objects.all()
        context['products'] = products
        context['categories'] = categories
        return context  
    

class ContactusView(View):
    template_name = 'general/contactus.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        email_from = settings.EMAIL_HOST_USER
        subject = f'feedback from {name}'
        send_mail(subject, message, email_from, [email])
        messages.success(request, "Send successfully")
        
        return render(request, self.template_name)
    
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = ProductModel.objects.filter(name__contains=query)
            return render(request, "general/search_list.html" ,{'products':products})
        else:
            print('No information')
            return render(request, "general/search_list.html" ,{})
        
        
    