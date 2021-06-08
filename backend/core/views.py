from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

from .models import Table, Reserve, Review, Product
from .serializers import TableSerializer




class MainPage(View):
    def get(self, request):
        reviews = Review.objects.all()
        products = Product.objects.all()
        context = {"reviews": reviews, "products": products}
        return render(request, 'core/index.html', context)

    def post(self, request):
        table_id = request.POST["table_num"]
        users = request.POST["people_num"]
        time = request.POST["time"]
        time = datetime.datetime.strptime(time, '%Y/%m/%d %H:%M')
        table = Table.objects.get(id=int(table_id))

        reserve = Reserve(
            number_of_users = int(users),
            table = table,
            order_user = request.user,
            date = time
        )
        reserve.save()

        table.status = "reserve"
        table.save()

        return HttpResponseRedirect(request.path_info)


@api_view(['GET'])
def tableListView(request):
    tables = Table.objects.all()
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)


class ReserveView():
    pass


class ReviewView():
    pass
