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

    context = {
        'title': title,
        'goods': goods,
    }
    return render(request, "fourth_task/shop.html", context)
