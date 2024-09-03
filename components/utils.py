import socket
import requests
import ipaddress
def get_device_ip():
    try:
        # Get the IP address of the device
        
        resp = requests.get("https://ifconfig.me/ip")
        ip_addr2 = resp.text
        return {"ip_address": ip_addr2}  # Return the ip_address
    except Exception as e:
        return {"ip_address": e}#"127.0.0.1"  # Fallback to localhost if IP can't be determined


import socket

hostname = socket.gethostname()
ip_addr = ipaddress.ip_address(socket.gethostbyname(hostname))


import requests

resp = requests.get("https://ifconfig.me/ip")
ip_addr2 = resp.text
if __name__ == "__main__":
    print(ip_addr)
    print(ip_addr2)