import socket

def is_network() -> bool:
    try:
        socket.gethostbyname("www.google.com")
        return True
    except:
        return False
    
print("le reseau est disponible.") if is_network() else print("le reseau est indisponible.")