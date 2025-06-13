from fabric.api import *
import time
import socket
def web():
    file_name= "2137_barista_cafe.zip"
    sudo("yum install httpd wget unzip -y")
    sudo("wget  https://www.tooplate.com/zip-templates/{} ".format(file_name))
    run("unzip {}".format(file_name))
    with lcd("./"):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)
    sudo("firewall-cmd --add-service=http --permanent")
    sudo("systemctl restart firewalld")
    sudo("systemctl restart httpd")
    time.sleep(10)
   # ipaddress = run("ip a | grep -i 192.168 | awk '{print $2}'")
    ipaddress = socket.gethostbyname(hostname)
    print("Done you can access the website by entering this : {}:80 on your browser".format(ipaddress))





