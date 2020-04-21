from django.shortcuts import render
from .Scripts import webscrap1
from .Scripts.logics import Calculations
# Create your views here.
def index(request):
    content = webscrap1.runstat()
    c1= Calculations(content)
    print(index)
    return render(request,'index1.html',{'s_no': c1.s_no(), 'States_UT': c1.state_ut(), 'Confirmed': c1.confirmed(), 'Recovered': c1.recovered(),
                     'Deceased': c1.deceased(), 'total_active':c1.total_active(),'total_confirmed':c1.total_confirmed(),'cured':c1.total_recovered(),'deaths':c1.total_death()})