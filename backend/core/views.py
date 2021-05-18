from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

from .models import Table, Reserve, Review




class MainPage(View):
    def get(self, request):
        reviews = Review.objects.all()
        context = {"reviews": reviews}
        return render(request, 'core/index.html', context)

    def post(self, request):
        pass



class TableListView(ListView):
    model = Table
    pass


class ReserveView():
    pass


class ReviewView():
    pass
