#es para poner ip  estatica por netplane
import subprocess
import os


#copia de seguridad
#subprocess.call(['sudo','cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.old'])
# file = open("/etc/netplan/50-cloud-init.yaml","w",'utf-8')
file = open("/etc/netplan/50-cloud-init.yaml","w")
#"pepino","tomate","lechuga",sep=", "
# file.write("network:\n")
# file.write("\b\b\bethernets:\n")
# file.write("\b\b\b\b\b\b\bethernets:\n")
# file.write("\b\b\b\b\b\b\b\b\b\baddresses: [jaja]\n")
# file.write("\b\b\b\b\b\b\b\b\b\bgateway4: 11516\n")
# file.write("\b\b\b\b\b\b\b\b\b\bdhcp4:false\n")
# file.write("\b\b\bversion:2\n")
print(os.system('ifconfig'))
print("dijite la interfas")
Interfas=input()
print("dijite la Ip statica ejem(192.168.1.20/24)")
ip=input()
print("dijite la gateway ejem(192.168.1.1)")
gateway=input()
file.write("network:\n")
file.write("    ethernets:\n")
file.write("       {0}:\n".format(Interfas))
file.write("          addresses: [{0}]\n".format(ip))
file.write("          gateway4: {0}\n".format(gateway))
file.write("          dhcp4: false\n")
file.write("    version: 2\n")
print(os.system('netplan apply'))
# linesFile = file.read() 
# print(str(linesFile))
file.close()
files = open("/etc/netplan/50-cloud-init.yaml","r")
linesFile = files.read() 
print(str(linesFile))