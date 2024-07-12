import bluetooth
import json
import os

def configure_wifi(ssid, password):
    wpa_supplicant_conf = "/etc/wpa_supplicant/wpa_supplicant.conf"

    # Append the new network configuration
    new_conf = f"""
    network={{
        ssid="{ssid}"
        psk="{password}"
        key_mgmt=WPA-PSK
    }}
    """

    with open(wpa_supplicant_conf, "a") as conf_file:
        conf_file.write(new_conf)

    # Restart the networking service
    os.system("sudo wpa_cli -i wlan0 reconfigure")

def bluetooth_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = bluetooth.PORT_ANY
    server_sock.bind(("", port))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    bluetooth.advertise_service(
        server_sock, "BluetoothServer",
        service_id = "00001101-0000-1000-8000-00805F9B34FB",
        service_classes = ["00001101-0000-1000-8000-00805F9B34FB", bluetooth.SERIAL_PORT_CLASS],
        profiles = [bluetooth.SERIAL_PORT_PROFILE]
    )

    print("Waiting for connection on RFCOMM channel", port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            print("Received:", data)
            credentials = json.loads(data.decode('utf-8'))
            ssid = credentials['ssid']
            password = credentials['password']
            configure_wifi(ssid, password)
    except OSError:
        pass

    print("Disconnected")
    client_sock.close()
    server_sock.close()
    print("Server stopped")

if __name__ == "__main__":
    bluetooth_server()
