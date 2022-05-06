import socket
import threading
from queue import Queue


def port_scan(target, port):
    try:
        this_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        this_socket.connect((target, port))
        return True
    except:
        return False


def fill_queue(ports, queue):
    for port in ports:
        queue.put(port)


def worker(target, queue, open_ports):
    while not queue.empty():
        port = queue.get()
        if port_scan(target, port):
            print(f'Port {port} is open!')
            open_ports.append(port)


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
        number = input(input_text)
        try:
            number = int(number)
        except:
            print('Port number is not valid.')
        return number


def main():
    target = get_ip('Enter the target IP address: ')
    number_of_threads = get_integer('Enter the number of threads: ')
    start_port_range = get_integer('Enter the starting port: ')
    end_port_range = get_integer('Enter the ending port: ')
    ports = range(start_port_range, end_port_range + 1)
    queue = Queue()
    open_ports = list()

    fill_queue(ports, queue)

    threads = list()
    for _ in range(number_of_threads):
        thread = threading.Thread(target=worker, args=(target, queue, open_ports))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Open ports are {open_ports}!')


if __name__ == '__main__':
    main()
