# 8-9 메시지
print("# 8-9 메시지")
msgs = ["hello", "hey", "bye bye"]

def show_messages(msgs):
    while msgs:
        msg = msgs.pop()
        print(msg)

show_messages(msgs)
print()

# 8-10 메시지 전송
print("# 8-10 메시지 전송")
msgs = ["hello", "hey", "bye bye"]
sent_messages = []

def show_messages(msgs, sent_messages):
    while msgs:
        msg = msgs.pop()
        print(msg)
        sent_messages.append(msg)

show_messages(msgs, sent_messages)
print()
print(msgs)
print(sent_messages)
print()

# 8-11 보관된 메시지
print("# 8-11 보관된 메시지")
msgs = ["hello", "hey", "bye bye"]
sent_messages = []

show_messages(msgs[:], sent_messages)
print()
print(msgs)
print(sent_messages)
print()