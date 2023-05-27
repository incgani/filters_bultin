from django.shortcuts import render

# Create your views here.
def Filter(request):
   import datetime
   do=datetime.datetime.now()
   d={'a':'my Name iS GaNesH','c':2,'do':do}
   return render(request,'filters.html',d)

