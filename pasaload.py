balance = 100

# function for sending pasaload
def send_pasaload(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Pasaload sent: {amount}")
    else:
        print("Insufficient balance")

# function for adding balance
def add_balance(amount):
    global balance
    balance += amount
    print(f"Balance added: {amount}")

if __name__ == '__main__':
    # add initial balance
    add_balance(100)

    # send pasaload
    send_pasaload(50)
    send_pasaload(30)

    # add balance again
    add_balance(20)

    # print the final balance
    print(f"Final balance: {balance}")
