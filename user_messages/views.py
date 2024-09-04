from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@csrf_exempt
def receive_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if name and email and content:
            Message.objects.create(name=name, email=email, content=content)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})














# from django.shortcuts import render, redirect
# from .forms import UserMessageForm
from django.shortcuts import render, redirect
# from .forms import UserMessageForm

# def send_message(request):
#     if request.method == 'POST':
#         form = UserMessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('message_sent')
        
#     else:
#         form = UserMessageForm()
#     return render(request, 'user_messages/send_message.html', {'form': form})        

# def message_sent(request):
#     return render(request, 'user_messages/message_sent.html')

# def send_message(request):
#     if request.method == 'POST':
#         form = UserMessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('message_sent')
        
#     else:
#         form = UserMessageForm()
#     return render(request, 'user_messages/send_message.html', {'form': form})        

# def message_sent(request):
#     return render(request, 'user_messages/message_sent.html')
