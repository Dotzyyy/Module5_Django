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
    messages = PrivateMessage.objects.filter(author=request.user).order_by('-timestamp')
    return render(request, 'private_message/sent_items.html', {'messages': messages})

@login_required
def view_item(request, pk):
    message = get_object_or_404(PrivateMessage, pk=pk)
    if message.recipient == request.user:
        message.is_read = True
        message.save()
    return render(request, 'private_message/view_item.html', {'message': message})

@login_required
def send_item(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save() 
            form.save_m2m()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'private_message/send_item.html', {'form': form})    
