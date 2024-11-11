from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, "third_task/main_page.html")


def basket_page(request):
    return render(request, "third_task/basket.html")


def shop_page(request):
    title = 'Перечень изделий, доступных для предзаказа'
    product1 = 'Полукруглое кресло (ольха)'
    product2 = 'Плечики напольные (бук)'
    product3 = 'Трон (массивный стул) (бук)'
    product4 = 'Рама фигурная с полочкой для зеркала (бук)'
    context = {
        'title': title,
        'product1': product1,
        'product2': product2,
        'product3': product3,
        'product4': product4,

    }
    return render(request, "third_task/shop.html", context)
