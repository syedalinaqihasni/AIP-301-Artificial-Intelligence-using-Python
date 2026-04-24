class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chatroom, content):
        message = Message(self, content)
        chatroom.add_message(message)


class Message:
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def display(self):
        print(f"{self.user.name}: {self.content}")


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined the chat.")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.name} left the chat.")

    def add_message(self, message):
        self.messages.append(message)

    def show_chat(self):
        print("\nChat History:")
        for msg in self.messages:
            msg.display()


# --- Testing

chatroom = ChatRoom()

user1 = User("Ali")
user2 = User("Sara")

chatroom.join(user1)
chatroom.join(user2)

user1.send_message(chatroom, "Hello everyone!")
user2.send_message(chatroom, "Hi Ali!")

chatroom.show_chat()

chatroom.leave(user2)