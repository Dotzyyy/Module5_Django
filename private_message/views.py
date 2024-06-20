from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PrivateMessage
from .forms import MessageForm

@login_required
def inbox(request):
    privatemessages = PrivateMessage.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'private_message/inbox.html', {'privatemessages': privatemessages})

@login_required
def sent_items(request):
    privatemessages = PrivateMessage.objects.filter(author=request.user).order_by('-timestamp')
    return render(request, 'private_message/sent_items.html', {'privatemessages': privatemessages})

@login_required
def view_item(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk)
    print(privatemessage)
    if privatemessage.recipient == request.user:
        privatemessage.is_read = True
        privatemessage.save()
    return render(request, 'private_message/view_item.html', {'privatemessage': privatemessage})

@login_required
def send_item(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            privatemessage = form.save(commit=False)
            privatemessage.author = request.user
            privatemessage.save() 
            form.save_m2m()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'private_message/send_item.html', {'form': form})    
