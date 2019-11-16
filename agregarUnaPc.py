######## ejemplo para dar ip a una maquina 
# host windows7-pc {
# hardware ethernet 00:0c:29:e6:75:b9;
# fixed-address 192.168.50.20;
# }
print("para saber cual es mi mac addres en otra PC (ifconfig | grep ether)")
print("dijite la mac de la PC que desea agregar")
mac=input()
print("nombre de la pc (pc1)")
nombre=input()
print("ip para esa maquina ")
ip=input()
dhcpd = open("/etc/dhcp/dhcpd.conf","a")
dhcpd.write('host {0} {1}\n'.format(nombre,chr(123)))
dhcpd.write('hardware ethernet {0} ;\n'.format(mac))
dhcpd.write('fixed-address {0} ;\n'.format(ip))
dhcpd.write('}\')
dhcpd.close()



