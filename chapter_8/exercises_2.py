def show_messages(messages):
    for message in messages:
        print(message)


to_show_messages = ['hello', 'hi', 'hiya', 'hallo']
show_messages(to_show_messages)


def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop()
        sent_messages.append(message)
    return sent_messages


to_send_messages = ['1', '2', '3', '4']
print(send_messages(to_send_messages[:]))
print(to_send_messages)
