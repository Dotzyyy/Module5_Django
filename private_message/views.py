from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import PrivateMessage
from .forms import MessageForm

@login_required
def inbox(request):
    privatemessages = PrivateMessage.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'private_message/inbox.html', {'privatemessages': privatemessages})

@login_required
def archive(request):
    privatemessages = PrivateMessage.objects.filter(recipient=request.user, archived=True)
    return render(request, 'private_message/archive.html', {'privatemessages': privatemessages})

@login_required
def delete_message(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk, recipient=request.user)
    if request.method == 'POST':
        privatemessage.delete()
        messages.success(request, f'Message "{privatemessage.subject}" deleted successfully!')
        return redirect('inbox')
    return redirect('inbox')  

@login_required
def item_confirm_delete(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk, recipient=request.user)
    return render(request, 'private_message/item_confirm_delete.html', {'privatemessage': privatemessage})

@login_required
def archive_message(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk, recipient=request.user)
    privatemessage.archived = True
    privatemessage.save()
    messages.success(request, f'Message "{privatemessage.subject}" archived successfully!')
    return redirect('inbox')

@login_required
def unarchive_message(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk, recipient=request.user)
    privatemessage.archived = False
    privatemessage.save()
    messages.success(request, f'Message "{privatemessage.subject}" unarchived successfully!')
    return redirect('archive')
    
    
    

@login_required
def sent_items(request):
    privatemessages = PrivateMessage.objects.filter(author=request.user).order_by('-timestamp')
    return render(request, 'private_message/sent_items.html', {'privatemessages': privatemessages})

@login_required
def view_item(request, pk):
    privatemessage = get_object_or_404(PrivateMessage, pk=pk)
    print(privatemessage)
    if privatemessage.recipient == request.user:
        privatemessage.unread = False
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

@login_required
def check_new_messages(request):
    new_messages_count = PrivateMessage.objects.filter(recipient=request.user, unread=True).count()
    return JsonResponse({'new_messages_count': new_messages_count})