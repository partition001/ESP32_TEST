import network
import socket
import uio


# Home Wi-Fi param

ssid = # your ssid
password = #your pass

# Connect to AP

def setup_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print('Connected to:', ssid)

    ip_address = wlan.ifconfig()[0]
    print('Your IP:', ip_address)

# Server request

def handle_request(client):
    try:
        data = client.recv(1024) 
        request_str = data.decode('utf-8')
        file_name = request_str.split(' ')[1][1:]
        if file_name == '':
            file_name = 'index.html'

        try:
            with uio.open('/data/{}'.format(file_name), 'r') as f:
                content = f.read()
                if file_name.endswith('.css'):
                    client.send('HTTP/1.1 200 OK\nContent-Type: text/css\n\n'.encode('utf-8') + content.encode('utf-8'))
                elif file_name.endswith('.html'):
                    client.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode('utf-8') + content.encode('utf-8'))
                else:
                    client.send('HTTP/1.1 404 Not Found\n\n'.encode('utf-8'))
        except:
            client.send('HTTP/1.1 404 Not Found\n\n'.encode('utf-8'))
    except OSError as e:
        if e.args[0] == errno.ECONNRESET:
            pass 
        else:
            raise

# Socket set

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)

setup_wifi(ssid, password)

while True:
    client, address = s.accept()
    handle_request(client)
    client.close()

