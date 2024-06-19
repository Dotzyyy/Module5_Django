from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PrivateMessage
from .forms import MessageForm

@login_required
def inbox(request):
    messages = PrivateMessage.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'private_message/inbox.html', {'messages': messages})

@login_required
def sent_items(request):
    messages = PrivateMessage.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messages_app/sent_items.html', {'messages': messages})

@login_required
def view_item(request):
    message = get_object_or_404(Message, pk=pk)
    if message.recipient == request.user:
        message.is_read = True
        message.save()
    return render(request, 'messages_app/view_item.html', {'message': message})

@login_required
def send_item(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.send = request.user
            message.save() 
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'private_message/send_item.html', {'form': form})    
