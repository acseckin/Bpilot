#! /bin/bash
echo "###################################################"
echo -e "\nUSB-Internet configuration begins"
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
route add default gw 192.168.7.1
echo -e "Finished\n"
echo "###################################################"
