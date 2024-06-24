
// Fetches the notification box and the message line

function newMessages(message) {
    const notificationContainer = document.getElementById('notification-container');
    const notificationMessage = document.getElementById('notification-message');
    notificationMessage.textContent = message;
    notificationContainer.style.display = 'block';
}

const messageList = document.getElementById('message-list');
const checkMessagesUrl = messageList.getAttribute('data-check-messages-url');

// checks whether there are messages with 'unread=True'
function checkForNewMessages() {
    fetch(checkMessagesUrl)
        .then(response => response.json())
        .then(data => {
            if (data.new_messages_count > 0) {
                newMessages(`You have ${data.new_messages_count} new message(s)!`);
            }
        });
}
    
setInterval(checkForNewMessages, 3000);  // runs the check code every 3 seconds


