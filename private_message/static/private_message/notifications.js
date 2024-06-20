



document.addEventListener('DOMContentLoaded', function() {
    // Example: Trigger notification when the page loads if there are unread messages
    var unreadMessages = {{ unread_messages|safe }};
    if (unreadMessages > 0) {
        showNotification('You have ' + unreadMessages + ' new messages.');
    }
});

function showNotification(message) {
    // Display the notification box
    var notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    document.body.appendChild(notification);

    // Automatically hide the notification after a few seconds (e.g., 5 seconds)
    setTimeout(function() {
        notification.style.display = 'none';
    }, 7500); 
}