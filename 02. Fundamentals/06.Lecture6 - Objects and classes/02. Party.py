class Party():
    def __init__(self):
        self.invites = []


party = Party()
while True:
    command = input()
    if command == "End":
        break
    party.invites.append(command)

print(f'Going: {", ".join(party.invites)}')
print(f'Total: {len(party.invites)}')
