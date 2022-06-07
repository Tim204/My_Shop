from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Category, Product
from cart.forms import CartAddProductForm
from .filters import ProductFilter
from django.db.models import Q 


def index(request):
    new_products = Product.objects.order_by('-created')[:6]
    queryset = Category.objects.all()
    return render(request, 'base.html', {'categories': queryset, 'new_products': new_products})




class SearchResulView(ListView):
    model = Product
    template_name = 'shop/product/search_results.html'
    context_object_name = 'search_results' 

    def get_queryset(self):
        return super().get_queryset().filter(
            name__icontains=self.request.GET.get('q')
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    


# Category slug parameter allows optional filtering by category
# category_slug parameter gives us the ability to optionally filter product by a give category
def product_list(request, category_slug=None,):
    category = None
    categories = Category.objects.all()

    # Available=True to filter only the available products
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    filtered_products = ProductFilter(request.GET, products)

    paginator = Paginator(filtered_products.qs, 9)  # Show 9 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'categories': categories,
        'filter': filtered_products,
        "page_obj": page_obj,

    }

    
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    # id and slug parameters in order to retrieve a product instance
    # Slug parameter added to make the SEO-friendly URLs for products
    product = get_object_or_404(
                                Product,
                                id=id,
                                slug=slug,
                                available=True
                                )
    # -> Adds the "add to cart form" to detail view
    cart_product_form = CartAddProductForm()

    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)
