from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from product.models import ProductModel
from product.forms import ProductForm
# Create your views here.

class ProductCreateView(CreateView):
    template_name = 'product/product_form.html'
    form_class = ProductForm
    success_url = "/"
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.uploaded_by = user
        return super().form_valid(form)

class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model =  ProductModel
    form_class = ProductForm
    
    

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = ProductModel
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = ProductModel.objects.all()
        context['products'] = products
        return context


class ProductUpdateView(UpdateView):
    template_name = 'product/product_form.html'
    model = ProductModel
    fields = "__all__"
    success_url = "/"


class ProductDeleteView(DeleteView):
    template_name = 'product/product_form.html'
    model = ProductModel
    form_class = ProductForm
    success_url = "/product/"
    
class ProductBuyView(View):
    template_name = 'product/product_buy.html'
    
    def get(self, request, pk):
        return render(request, self.template_name)
    
    def post(self, request, pk):

        return render(request, self.template_name)
    

