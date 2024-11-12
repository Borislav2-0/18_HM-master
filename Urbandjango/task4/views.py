from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    context = {
        "title": title
    }
    return render(request, "fourth_task/main_page.html", context)


def basket_page(request):
    title = 'Корзина'
    context = {
        "title": title
    }
    return render(request, "fourth_task/basket.html", context)


def shop_page(request):
    title = 'Перечень изделий, доступных для предзаказа'
    goods = ['Полукруглое кресло (ольха)',
             'Плечики напольные (бук)',
             'Трон (массивный стул) (бук)'
             'Рама фигурная с полочкой для зеркала (бук)'
             ]
    # product1 = 'Полукруглое кресло (ольха)'
    # product2 = 'Плечики напольные (бук)'
    # product3 = 'Трон (массивный стул) (бук)'
    # product4 = 'Рама фигурная с полочкой для зеркала (бук)'
    context = {
        'title': title,
        'goods': goods,
        # 'product1': product1,
        # 'product2': product2,
        # 'product3': product3,
        # 'product4': product4,

    }
    return render(request, "fourth_task/shop.html", context)
