from django.views.generic import ListView
from .models import Wish


class IndexView(ListView):
    model = Wish
    template_name = 'wishlist/index_view.html'
