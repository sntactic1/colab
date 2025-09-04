import socket

def is_network(url : str) -> bool:
    try:
        socket.gethostbyname(url)
        return True
    except:
        return False
    finally:
        pass
    

urlToCheck = ["www.google.com" , "www.aws.com" , "www.coursera.com"]

for url in urlToCheck:
    if is_network(url):
        print(url , " est disponible.")
    else:
        print(url ," est indisponible.")