def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello, how are you?", "Have a great day!", "Keep working hard!", "Python is fun!", "Never give up!"]
sent_messages = []
send_messages(messages[:], sent_messages)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)