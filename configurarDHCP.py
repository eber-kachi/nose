import subprocess
import os
def menu(mensajes):
    cont=1
    for  mensaje in mensajes:
        print("==##( {0}. {1} )##== ".format(cont, mensaje))
        cont+=1

    #print("==##( 0. Salir )##==")
print(os.system('ifconfig'))
menu(['dijite nombre de la interfas para la configuracion ejem(enp0s3)'])
defaul=input()
files = open("/etc/default/isc-dhcp-server","w")
files.write('INTERFACESv4="{0}"\n'.format(defaul))
files.write('INTERFACESv6=""')
files.close()
#configurando archivo dhcpd.conf
print('dijite el rango de Ip ejem(192.168.1.0)')
rango=input()
print('dijite la macara ejem(255.255.255.0)')
mask=input()
print('dijite el inicio de IP ejem(192.168.1.5)')
inicio=input()
print('dijite el fin de la IP ejem(192.168.1.100)')
fin=input()
print('dijite IP router ejem(192.168.1.1))')
router=input()
dhcpd = open("/etc/dhcp/dhcpd.conf","w")
dhcpd.write('default-lease-time 600;\n')
dhcpd.write("max-lease-time 7200;\n")
dhcpd.write("ddns-update-style none;\n")
dhcpd.write("authoritative;\n\n\n")
#subnet  192.168.1.0 rango de ip
dhcpd.write('subnet {0} netmask {1} {2}\n'.format(rango,mask,chr(123)))
dhcpd.write(" range {0} {1};\n".format(inicio,fin))
dhcpd.write(" option routers {0};\n".format(router))
dhcpd.write(" option subnet-mask {0};\n".format(mask))
dhcpd.write(" option domain-name-servers {0}, 8.8.8.8;\n".format(router))
dhcpd.write("}")
dhcpd.close()

print(os.system('sudo systemctl restart isc-dhcp-server')) 
print(os.system('sudo systemctl status isc-dhcp-server')) 

# print(os.system('sudo systemctl restart isc-dhcp-server')) 
########## ejemplo para dar ip a una maquina 
# host windows7-pc {
# hardware ethernet 00:0c:29:e6:75:b9;
# fixed-address 192.168.50.20;
# }















