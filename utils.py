import socket

def get_device_ip():
    try:
        # Get the IP address of the device
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return {"ip_address": ip_address}  # Return the ip_address
    except Exception as e:
        return {"ip_address": "127.0.0.1"}#"127.0.0.1"  # Fallback to localhost if IP can't be determined
