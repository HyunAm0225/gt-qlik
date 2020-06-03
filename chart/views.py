from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib import messages
from accounts.decorators import *
from accounts.models import User

from .forms import ChartWriteForm
from .models import Chart
# Create your views here.

@method_decorator(login_message_required, name='dispatch')
class chartListView(ListView):
    model = Chart
    paginated_by = 10
    template_name = 'chart_list.html'
    context_object_name = 'chart_list'

    def get_queryset(self):
        chart_list = Chart.objects.order_by('chart_rank')
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

    return context

@login_message_required
def chart_detail_view(request,pk):
    chart = get_object_or_404(Chart,pk=pk)
    
    if request.user == chart.chart_writer:
        chart_auth = True
    else:
        chart_auth = False
    
    context = {
        'chart' : chart,
        'chart_auth' : chart_auth
    }
    return render(request, 'chart_detail.html',context)


@admin_required
@login_message_required
def chart_write_view(request):
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
@admin_required
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
@admin_required
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
def chart_report(request):
    chart_list = Chart.objects.filter(chart_writer=request.user).order_by('chart_rank')
    return render(request,'chart_report.html',{'chart_list':chart_list})