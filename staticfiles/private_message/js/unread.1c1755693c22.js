document.addEventListener('DOMContentLoaded', function () {
    const inboxItem =document.querySelectorAll('.inbox-list-item');

    inboxItem.forEach(function (message) {  // Detecting whether unread == True on the privateMessage model
        if (message.getAttribute('data-unread') == 'True') {
            message.classList.add('unread');
        }
    })
})