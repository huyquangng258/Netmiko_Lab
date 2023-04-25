from netmiko import ConnectHandler

#dictionary, object
Router = {
    "device_type": "cisco_ios",
    "ip": "192.168.248.133",
    "username": "vnpro",
    "password": "vnpro@123",
    "secret": "vnpro@321" #password enable
}

#user, privileges, config

connect = ConnectHandler(**Router) #unpack , re use

connect.enable()

# send_command function
print(connect.send_command("show run"))

# send_config_set function
print(connect.send_config_set("hostname R1-Netmiko-Python"))

print(connect.send_config_set(["int e0/2", "no shut", "ip add 192.168.2.1 255.255.255.0"]))

# use for loop
for i in range(1, 4):
    print(connect.send_config_set(["int e0/" + str(i), "no shut", "ip add 192.168."+ str(i) +".1 255.255.255.0"]))
    
print(connect.send_command("show ip int bri"))

# string, interger, float(1.2, 8.4)   w3shool
# concatenate, parse(convert)

"""
e0/1: 192.168.12.1
e0/2: 192.168.15.5
e0/3: 192.168.21.3
"""
interfaces = {
    "e0/1": "192.168.12.1",
    "e0/2": "192.168.15.5",
    "e0/3": "192.168.21.3"
}


for i in interfaces:
    print(connect.send_config_set(["int " + i, "ip address " + interfaces[i] + " 255.255.255.0", "no shut"]))
print(connect.send_command("show ip int bri"))

#disconnect
connect.disconnect()

## input, output


#Variables Scopes
#global
#local i