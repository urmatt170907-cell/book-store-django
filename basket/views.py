from django.urls import reverse_lazy
from django.views import generic

from .models import Basket
from .forms import BasketForm


class BasketListView(generic.ListView):
    model = Basket
    template_name = "basket/basket_list.html"
    context_object_name = "baskets"
    paginate_by = 5
    ordering = ["-id"]


class BasketCreateView(generic.CreateView):
    model = Basket
    form_class = BasketForm
    template_name = "basket/create_basket.html"
    success_url = reverse_lazy("basket_list")


class BasketUpdateView(generic.UpdateView):
    model = Basket
    form_class = BasketForm
    template_name = "basket/update_basket.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("basket_list")


class BasketDeleteView(generic.DeleteView):
    model = Basket
    pk_url_kwarg = "id"
    success_url = reverse_lazy("basket_list")