
m fabric.api import *
import time
def web():
    file_name= "2137_barista_cafe.zip"
    print("Installing tools")
    sudo("yum install httpd wget unzip -y")
    sudo("wget  https://www.tooplate.com/zip-templates/{} ".format(file_name))
    run("unzip {}".format(file_name))
    sudo("rm -rf /var/www/html/*")
    sudo("mv {}/* /var/www/html/".format(file_name[:-4]))
    sudo("yum install firewalld -y")
    sudo("firewall-cmd --add-service=http --permanent")
    sudo("systemctl restart firewalld")
    sudo("systemctl restart httpd")
    time.sleep(10)
    ipaddress = run("ip a | grep -i 192.168 | awk '{print $2}'")
    print("Done you can access the website by entering this : {}:80 on your browser".format(ipaddress))
