# Created by Bruce at 11/7/2022
import requests
import scapy.all as scapy
import socket


# device_host: the hostname/IP of the device
# server_address: the hostname/IP of the control hub
# server_port: the port of the APIs
# mqtt_username: the username of the mqtt broker
# mqtt_password: the password of the mqtt broker
# door_direction: right = 1, left = - 1
# selected_module: None = 0, RFID = 1, Keypad = 2


def pairing(
    device_host,
    server_address,
    server_port,
    mqtt_username,
    mqtt_password,
    door_direction=1,
    selected_module=1,
):
    url = device_host + "/pairing"

    request_body = {
        "serverAddress": server_address,
        "serverPort": server_port,
        "doorDirection": door_direction,
        "selectedModule": selected_module,
        "mqttUsername": mqtt_username,
        "mqttPassword": mqtt_password,
    }

    result = requests.post(url, json=request_body)
    resp = result.json()

    device_id = ""
    if result.status_code == 200:
        device_id = resp["deviceID"]
        print("The paired device:" + device_id)
    else:
        print("status code:" + str(result.status_code))
        print("Pairing error:" + resp["message"])

    return device_id


def _scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=0.25,
        verbose=False,
    )[0]

    clients_list = []
    for element in answered_list:
        mac = element[1].hwsrc
        client_dict = {
            "deviceId": mac.replace(":", ""),
            "ip": element[1].psrc,
        }
        clients_list.append(client_dict)
    return clients_list


def get_device():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    ip_prefix = local_ip[: local_ip.rfind(".") + 1]
    scanned_device = []
    for i in range(0, 256):
        curr_ip = ip_prefix + str(i)
        scan_result = _scan(curr_ip)
        if scan_result:
            scanned_device.extend(scan_result)

    return scanned_device
