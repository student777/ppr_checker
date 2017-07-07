from django.shortcuts import render
from .models import Deal, Goods


def index(request):
    name = request.GET.get('name')
    if name is None:
        goods_deals = None
    else:
        goods_iist = Goods.objects.filter(name__contains=name)
        goods_deals = []
        for goods in goods_iist:
            deals = Deal.objects.filter(goods=goods, is_available=True)
            goods_deals.append((goods, deals))
    return render(request, 'index.html', {'goods_deals': goods_deals})
