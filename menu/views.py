from django.shortcuts import render
from django.views.generic import ListView
from .models import Menu
from accounts.decorators import *
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
# Create your views here.

@method_decorator(login_message_required, name='dispatch')
class MenuListView(ListView):
    model = Menu
    paginated_by = 10
    template_name = 'menu_list.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        menu_list = Menu.objects.order_by('menu_rank')
        return menu_list

def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    paginator = context['paginator']
    page_numbers_range = 5
    max_index = len(paginator.page_range)

    page = self.request.GET.get('page')
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    context['page_range'] = page_range

    return context

@login_message_required
def menu_detail_view(request,pk):
    menu = get_object_or_404(Menu,pk=pk)
    context = {
        'menu' : menu,
    }
    return render(request, 'menu_detail.html',context)