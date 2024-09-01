
password = input("Enter The Master Password : If Using First Time Create A Password ")


mode = input("Do You Want to enter a new password or view existing one (view,add): ")

def add():
    name = input("Enter Name Of Account : ")
    platform = input("Which Platform is it: for example Instagram or Facebook or else : ")
    passw = input("Enter Password You Want to Store : ")
    with open("password.txt", "a") as f:
        f.write(f"This Is Your Password Of {platform}\nName: {name}\nPassword: {passw}\n\n")

def view():
    try:
        with open("password.txt", "r") as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("No passwords stored yet.")
    except FileNotFoundError:
        print("No password file found. Add a password first.")

if mode == "view":
    view()
elif mode == "add":
    add()
else:
    print("Invalid mode")
