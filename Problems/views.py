from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Problems.models import ProblemSet
from Problems import littlechecker as lc
import subprocess
from .forms import SubmissionForm

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
        form =SubmissionForm()
        return render(request, 'problemPage.html', {'problem': problem,'form':form})
    except:
        return render(request, 'index.html')

def problemSubmit(request,problemID):
    language,codeFile = None,None
    print("$")
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        print("%")
        if form.is_valid():
            print("^")
            language = request.POST.get("language",None)
            for fields in form:
                codeFile=fields
    if language == None or codeFile == None:
        print("))")
        return render(request,'submit.html',{'problemID': problemID, 'returnStatus': 1})
    else:
        print(lc.compile('tests.c',language))
        #write code for system check
        return render(request,'submit.html',{'problemID': problemID, 'returnStatus': 1})


