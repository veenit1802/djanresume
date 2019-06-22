from django.shortcuts import render
def load(request):
    #loads the html page
    d={"name":"Veenit ","email":"veenitshukla20@gmail.com","phone":"7355752272","link":"https://www.linkedin.com/in/veenit-shukla-05aab115a/","git":"https://github.com/veenit1802","twi":"https://twitter.com/veenitshukla20"}
    return render(request,'index.html',d)