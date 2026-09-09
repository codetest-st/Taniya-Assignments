user="Alice"
def sayhello():
    global user
    user="Jatin"
    print(f"Hello,{user}!,{globals()['user']}")

sayhello()
print(user)

