from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def create_basket_view(request):
    if request.method == 'POST':
        form = forms.BasketForm(
            request.POST
        )

        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else:
        form = forms.BasketForm()

    context = {
        'form': form
    }

    return render(
        request,
        'basket/create_basket.html',
        context
    )


def basket_list_view(request):
    baskets = models.Basket.objects.all().order_by('-id')

    context = {
        'baskets': baskets
    }

    return render(
        request,
        'basket/basket_list.html',
        context
    )


def update_basket_view(request, id):
    basket = get_object_or_404(
        models.Basket,
        id=id
    )

    if request.method == 'POST':
        form = forms.BasketForm(
            request.POST,
            instance=basket
        )

        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else:
        form = forms.BasketForm(
            instance=basket
        )

    context = {
        'form': form,
        'basket': basket
    }

    return render(
        request,
        'basket/update_basket.html',
        context
    )


def delete_basket_view(request, id):
    basket = get_object_or_404(
        models.Basket,
        id=id
    )

    basket.delete()

    return redirect('/basket_list/')