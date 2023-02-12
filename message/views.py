from django.shortcuts import render
from . import chatBotModel

chatHist_temp =chatBotModel.chatHist()
# Create your views here.
def index(request):
  if request.method=='POST':
        user_message=request.POST.get('val1')
        print(user_message)
        chatHist_temp.make_list(user_message)
  return render(request,"index.html",{'messageHist':chatHist_temp.get_list()})