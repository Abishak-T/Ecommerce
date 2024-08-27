from django.shortcuts import render,redirect
from app.forms import AppForm,SubForm,SignupForm
from app.models import AppModel,SubModel,SignupModel

# Create your views here.



 #home page
def home(request):
    return render(request,"index.html")

# fot main category datas
def register(request):
    print(request.POST)
    print(request.FILES)
    
    if request.method == "POST":
        form=AppForm(request.POST,request.FILES)
        if form.is_valid():
            print("hii")
            form.save()
            print("save")
            return redirect("display")
        else:
            return render(request,"firstpg.html")
    return render(request,"firstpg.html")
   
#  main category display
def displayview(request):
    data=AppModel.objects.all()
    print(data)
    return render(request,"displaypg.html",{"data":data})


# def detailview(request,id):
#     view=AppModel.objects.get(id=id)
#     return render(request,"subcat.html",{"view":view})
    
            
def updatedata(request,id):
      print(request.POST)
      print(request.FILES)
      updt=AppModel.objects.get(id=id)   
      if request.method == "POST":
        form=AppForm(request.POST,request.FILES,instance=updt)  
        if form.is_valid():
            form.save()
            return redirect("display")
      else:
          form=AppForm(instance=updt)
      return render(request,"updatedata.html",{"form":form})
  
  
#for delete option

def deletedata(id):
    AppModel.objects.get(id=id).delete()
    return redirect('display')
      
      
      
                                    #  subcategory
#   for subcategory datas   
def subregister(request):
    print(request.POST)
    print(request.FILES)
    
    if request.method == "POST":
        form=SubForm(request.POST,request.FILES)
        if form.is_valid():
            print("hii")
            form.save()
            print("save")
            return redirect("homee")
        else:
          data=AppModel.objects.all()      
          cat_value=[i.category for i in data]  
          return render(request,'subregpage.html',{"form":form,"cat_value":cat_value})
    else:
        form=SubForm
        data=AppModel.objects.all()
        cat_value=[i.category for i in data]
        return render(request,'subregpage.html',{"form":form,"cat_value":cat_value})
 


#  subcategory display
def subcat(request,category):
    subdata=SubModel.objects.filter(category=category)
    print("hi")
    return render(request,"subcat.html",{"subdata":subdata})        
            
# subcategory edit & update        

def subupdatedata(request,id):
    print(request.POST)
    print(request.FILES)
    subupdt=SubModel.objects.get(id=id)
    print(subupdt)   
    if request.method == "POST":
        print(request.POST)
        form=SubForm(request.POST,request.FILES,instance=subupdt)  
        if form.is_valid():
            form.save()
            return redirect("homee")
        else:
            data=AppModel.objects.all()
            print(data)      
            cat_value=[i.category for i in data]  
            return render(request,'subupdate.html',{"form":form,"cat_value":cat_value})
    else:
        form=SubForm(instance=subupdt)
        data=AppModel.objects.all()
        print(data)
        cat_value=[i.category for i in data]
        return render(request,'subupdate.html',{"form":form,"cat_value":cat_value})
  
# subcategory delete  
def subdelete(request,id):
    SubModel.objects.get(id=id).delete()
    return redirect('display')

#signup function
def signup(request):
    if request.method == "POST":
        print(request.POST)
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"signup.html")
    return render(request,"signup.html")
        
        
 #login fnctn   
def login(request):
    if request.method== "POST":
        print(request.POST)
        if SignupModel.objects.filter(signemail=request.POST['logemail']).exists():
            sig=SignupModel.objects.get(signemail=request.POST['logemail'])
            if sig.signpass==request.POST['logpass']:
                return redirect('homee')
    return render(request,'login.html')


    

#details viewing

def detailsdispl(request,id):
    det=SubModel.objects.get(id=id)
    return render(request,"detailspage.html",{"det":det}) 
    