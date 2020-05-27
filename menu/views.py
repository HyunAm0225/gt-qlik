from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from accounts.decorators import *
from accounts.models import User

from .forms import MenuWriteForm
from .models import Menu

# Create your views here.

@method_decorator(login_message_required, name='dispatch')
class MenuListView(ListView):
    model = Menu
    paginated_by = 10
    template_name = 'menu_list.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        menu_list = Menu.objects.filter(writer=self.request.user).order_by('menu_rank')
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


@login_message_required
def menu_write_view(request):
    if request.method == "POST":
        form = MenuWriteForm(request.POST)
        # 아이디 호출
        # user = request.session['username']
        # print(user)
        # username = User.objects.get(username = user)

        if form.is_valid():
            menu = form.save(commit = False)
            menu.writer = request.user
            menu.save()
        return redirect('menu:menu_list')

    else:
        form = MenuWriteForm()

    return render(request,"menu_write.html",{'form':form})
