from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib import messages
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
    
    if request.user == menu.writer:
        menu_auth = True
    else:
        menu_auth = False
    
    context = {
        'menu' : menu,
        'menu_auth' : menu_auth
    }
    return render(request, 'menu_detail.html',context)


@login_message_required
def menu_write_view(request):
    if request.method == "POST":
        form = MenuWriteForm(request.POST)
        if form.is_valid():
            menu = form.save(commit = False)
            menu.writer = request.user
            menu.save()
        return redirect('menu:menu_list')

    else:
        form = MenuWriteForm()

    return render(request,"menu_write.html",{'form':form})

# 메뉴 수정

@login_message_required
def menu_edit_view(request, pk):
    menu = Menu.objects.get(id=pk)

    if request.method == "POST":
        if(menu.writer == request.user):
            form = MenuWriteForm(request.POST,instance = menu)
            if form.is_valid():
                menu = form.save(commit = False)
                menu.save()
                messages.success(request,"수정되었습니다.")
                return redirect('/menu/'+str(pk))
    else:
        menu = Menu.objects.get(id=pk)
        if menu.writer == request.user:
            form = MenuWriteForm(instance = menu)
            context = {
                'form':form,
                'edit':'수정하기',
            }
            return render(request, "menu_write.html",context)
        else:
            messages.error(request,"본인 메뉴가 아닙니다.")
            return redirect('/menu/'+str(pk))

# 메뉴 삭제

@login_message_required
def menu_delete_view(request,pk):
    menu = Menu.objects.get(id=pk)
    if menu.writer == request.user:
        menu.delete()
        messages.success(request,"삭제되었습니다.")
        return redirect('/menu/')
    else:
        messages.error(request, "본인 메뉴가 아닙니다.")
        return redirect('/menu/'+str(pk))