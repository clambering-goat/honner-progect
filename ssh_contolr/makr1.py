

import paramiko

USER = 'pi'
PASSWORD = '539620785'

commands = ["cd Desktop/", "python3 film_clint.py"]
ip_list=[".240",".108",".227"]


for ips in ip_list:
    HOST='192.168.1'+ips
    print("conneting to ",HOST)
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(HOST, port=22, username=USER, password=PASSWORD)

    channel = client.get_transport().open_session()
    channel.invoke_shell()


    while channel.recv_ready():
        info=channel.recv(1024)
        print(info)


    for loop1 in commands:
        data=loop1+"\n"
        channel.sendall(data)
