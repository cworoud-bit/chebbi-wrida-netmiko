from netmiko import ConnectHandler

def acces_netmiko():
    cisco_router = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
        "secret": "",
    }

    net_connect = ConnectHandler(**cisco_router)
    
    # Affiche l'heure du routeur
    print(net_connect.send_command("show clock"))
    
    # Récupère les interfaces
    interfaces = net_connect.send_command("show ip interface brief")
    
    # Écrit les interfaces dans un fichier
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)  # <-- ici on complète avec write()

# Appel de la fonction
acces_netmiko()
