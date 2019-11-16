# script para  crear virtual host 

import os

# metodo para limpiar la pantalla
def cls():
     os.system('cls')
# metodo para menu dinamico 
def menu(mensajes):
    cont=1
    for  mensaje in mensajes:
        print("•÷±‡±( {0}. {1} )±‡±÷ ".format(cont, mensaje))
        cont+=1
    print("•÷±‡±( 0. Salir )±‡±÷ ")
#  os.system('ipconfig /flushdns')
menu(['Crear Virtual Host','Salir'])
opction=input()
if(opction):
  print("nombre del dominio kantuta.com")
  dominio=input()
  # code basic html
  html='<!DOCTYPE html>\n<html lang="es">\n<head>\n <meta charset="UTF-8">\n <meta name="viewport" content="width=device-width, initial-scale=1.0">\n <meta http-equiv="X-UA-Compatible" content="ie=edge">\n <title>{0}</title>\n</head>\n<body>\n <h1>{0}</h1>\n</body>\n</html>'.format(dominio)
  os.system("sudo mkdir -p /var/www/{0}/public".format(dominio))
  os.system("sudo chown -R $USER:$USER /var/www/{0}/public".format(dominio))
  os.system("sudo chmod -R 755 /var/www/{0}".format(dominio))
  file = open("/var/www/{0}/public/index.html".format(dominio), "w")
  file.write(html)
  # file.write(" <title>{0}</title>\n".format(dominio))
  # file.write("</head>\n<body>\n <h1>{0}</h1>\n</body>\n</html>".format(dominio))
  file.close()
  # serverAdmin=input()
  fileDominio=open("/etc/apache2/sites-available/{0}.conf".format(dominio),"w")
  fileDominio.write("<VirtualHost *:80>\n")
  fileDominio.write(" ServerAdmin admin@{0}\n".format(dominio))
  fileDominio.write(" ServerName {0}\n".format(dominio))
  fileDominio.write(" ServerAlias www.{0}\n".format(dominio))
  fileDominio.write(" DocumentRoot /var/www/{0}/public\n".format(dominio))
  fileDominio.write(" ErrorLog ${APACHE_LOG_DIR}/error.log\n")
  fileDominio.write(' CustomLog ${APACHE_LOG_DIR}/access.log combined\n')
  fileDominio.write("</VirtualHost>\n")
  fileDominio.close()
  os.system("sudo a2ensite {0}.conf".format(dominio))
  # os.system("sudo a2dissite 000-default.conf")#solo la primera ves
  print(os.system("sudo apache2ctl configtest"))
  print(os.system("sudo systemctl restart apache2"))




