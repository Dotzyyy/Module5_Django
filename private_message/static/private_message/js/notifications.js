


function showNotification(message) {
    const notificationContainer = document.getElementById('notification-container');
    const notificationMessage = document.getElementById('notification-message');
    notificationMessage.textContent = message;
    notificationContainer.style.display = 'block';
}

const messageList = document.getElementById('message-list');
const checkMessagesUrl = messageList.getAttribute('data-check-messages-url');

function checkForNewMessages() {
    fetch(checkMessagesUrl)
        .then(response => response.json())
        .then(data => {
            if (data.new_messages_count > 0) {
                showNotification(`You have ${data.new_messages_count} new message(s)!`);
            }
        });
}
    
setInterval(checkForNewMessages, 1000);  // Check for new messages every 5 seconds