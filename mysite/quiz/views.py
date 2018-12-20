from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import QuizItem

def myView(request):
    all_quiz_items = QuizItem.objects.all()
    return render(request, 'quiz.html', 
        {'all_items': all_quiz_items})

def addQuiz(request):
    # create a new quiz all_items
    new_item = QuizItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect the browser to '/quiz/'
    return HttpResponseRedirect('/quiz/')

def deleteQuiz(request, quiz_id):
    item_to_delete = QuizItem.objects.get(id=quiz_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/quiz/')


