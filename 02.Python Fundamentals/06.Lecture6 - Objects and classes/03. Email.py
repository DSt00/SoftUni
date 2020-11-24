class Email:
    def __init__(self, s, r, c):
        self.is_send = False
        self.sender = s
        self.receiver = r
        self.content = c

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []
while True:
    command = input()
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)

send = input().split(", ")
send = [int(x) for x in send]

for index in send:
    emails[index].send()

for mail in range(len(emails)):
    print(emails[mail].get_info())
