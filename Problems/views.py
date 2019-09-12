from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Problems.models import ProblemSet
import subprocess

# Create your views here.
def problemIndex(request):
    print("aaaaa")
    problems = ProblemSet.objects.all()
    print(problems)
    badgeCount = {}
    for i in problems:
        tags = i.tags.split()
        for j in tags:
            if j in badgeCount:
                badgeCount[j] += 1
            else:
                badgeCount[j] = 1
    print("bbb")
    return render(request, 'problems.html' , {'problems': problems, 'badgeCount': badgeCount} )

def problemWithID(request,problemID):
    try:
        problem = ProblemSet.objects.get(pk = problemID)
        return render(request, 'problemPage.html', {'problem': problem})
    except:
        return render(request, 'index.html')

def problemSubmit(request,problemID):
    language,codeFile = None,None
    if request.method == "POST":
        language = request.POST.get("language",None)
        codeFile = request.POST.get("codeFile",None)
    if language == None or codeFile == None:
        return render(request,'submit.html',{'problemID': problemID, 'returnStatus': 1})
    else:
        x = 0
        #write code for system check