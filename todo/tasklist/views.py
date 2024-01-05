from django.shortcuts import render

def index(request):
    return render(              # returns HttpResponse
        request,                # Запрос в точности, как вы его получили
        'tasklist/index.html', 
        {
            # 'var': param
        }
    )


def add_task(request):
    if request.method == 'POST':
        print(request.POST)
        task_data = TaskForm(request.POST)
        if task_data.is_valid():
             print(task_data.cleaned_data)
    task_form = TaskForm()
    return render(            
        request,         
        'tasklist/form.html',
        {
           'task_form_auto_gen': task_form
        }
    )
    