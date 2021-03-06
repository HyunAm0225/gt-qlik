from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from accounts.decorators import *
from accounts.models import User
from cart.models import Cart, CartItem
from menu.models import Menu



from .forms import ChartWriteForm
from .models import Chart
# Create your views here.

@method_decorator(login_message_required, name='dispatch')
class chartListView(ListView):
    model = Chart
    paginate_by = 10
    template_name = 'chart_list.html'
    context_object_name = 'chart_list'

    def get_queryset(self):
        if self.request.user.is_superuser:
            chart_list = Chart.objects.order_by('chart_rank')
        else:
            chart_list = Chart.objects.filter(chart_writer=self.request.user).order_by('chart_rank')[:6]
        return chart_list

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

        menu_list = Menu.objects.order_by('menu_rank')
        context['menu_list'] = menu_list

        return context

@login_message_required
def chart_detail_view(request,pk):
    chart = get_object_or_404(Chart,pk=pk)
    menu_list = Menu.objects.order_by('menu_rank')
    chart_list = set(Chart.objects.order_by('chart_rank'))
    if request.user == chart.chart_writer:
        chart_auth = True
    else:
        chart_auth = False
    
    context = {
        'chart' : chart,
        'chart_auth' : chart_auth,
        'menu_list' : menu_list,
        'chart_list' : chart_list
    }
    return render(request, 'chart_detail.html',context)


# @admin_required
@login_message_required
def chart_write_view(request):
    if Chart.objects.filter(chart_writer=request.user).count() > 5:
        return redirect('chart:chart_list')  
    if request.method == "POST":
        form = ChartWriteForm(request.POST)
        if form.is_valid():
            chart = form.save(commit = False)
            chart.chart_writer = request.user
            chart.save()
        return redirect('chart:chart_list')

    else:
        form = ChartWriteForm()

    return render(request,"chart_write.html",{'form':form})


# 차트 수정
# @admin_required
@login_message_required
def chart_edit_view(request, pk):
    chart = Chart.objects.get(id=pk)

    if request.method == "POST":
        if(chart.chart_writer == request.user):
            form = ChartWriteForm(request.POST,instance = chart)
            if form.is_valid():
                chart = form.save(commit = False)
                chart.save()
                messages.success(request,"수정되었습니다.")
                return redirect('/chart/'+str(pk))
    else:
        chart = Chart.objects.get(id=pk)
        if chart.chart_writer == request.user:
            form = ChartWriteForm(instance = chart)
            context = {
                'form':form,
                'edit':'수정하기',
            }
            return render(request, "chart_write.html",context)
        else:
            messages.error(request,"본인 차트가 아닙니다.")
            return redirect('/chart/'+str(pk))    

# 메뉴 삭제
# @admin_required
@login_message_required
def chart_delete_view(request,pk):
    chart = Chart.objects.get(id=pk)
    if chart.chart_writer == request.user:
        chart.delete()
        messages.success(request,"삭제되었습니다.")
        return redirect('/chart/')
    else:
        messages.error(request, "본인 차트가 아닙니다.")
        return redirect('/chart/'+str(pk))

@login_message_required
# def chart_report(request):
def chart_report(request,cart_items = None):
    menu_list = Menu.objects.order_by('menu_rank')
    chart_list = Chart.objects.filter(chart_writer=request.user).order_by('chart_rank')[:6]
    print(chart_list)
    return render(request,'chart_report.html',dict(chart_list=chart_list,menu_list=menu_list))

    