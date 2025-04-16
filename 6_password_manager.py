from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    with open('key.key','rb') as k:
        key = k.read()
        return key


key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            passw = fer.decrypt(passw.encode()).decode()
            print('User:', user,'| Password:',passw )

def add():
    name= input('Account name: ')
    pwd= input('Password: ')
    with open('password.txt', 'a') as f:
        f.write(name + "|"+ fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input('would you like to add a new password or view old password or q to quit(view, add, q)? ').lower()
    if mode =='q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else: 
        print('invalid option!')
        continue


print('Thank you for using.')