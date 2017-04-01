#! /bin/bash

echo -"USB-Internet configuration begins"
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
route add default gw 192.168.7.1
echo -e "Internet configuration finished\n"

echo "Updating"
sudo apt-get update
echo -e "\n Language settings: en_US.UTF-8 \n"
sudo locale-gen en_US.UTF-8
echo -e "\n ntpdate install and get date"
sudo apt-get install ntpdate -y
sudo ntpdate pool.ntp.org
sudo apt-get update
echo -e "\n Essentials \n"
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y
sudo apt-get install gfortran libatlas-base-dev python-pip python-dev -y
sudo apt-get install python-numpy -y
sudo apt-get install python-scipy -y
sudo apt-get install python-matplotlib -y

echo -e "\n Adafruit BBIO installation \n"
sudo pip install --upgrade pip
sudo pip install Adafruit_BBIO

sudo pip install pyserial
sudo pip install numpy
sudo pip install scipy
sudo pip install matplotlib
sudo pip install scikit-fuzzy

echo -e "\n Slots configuration check \n"
cd /sys/devices/platform/bone_capemgr
File=slots
if grep -q "Override Board Name,00A0,Override Manuf,univ-emmc" "$File"; 
then    
        cd
        echo -e "\nHooray!! configuration available"
        echo -e "\n UART 4 configuration p9.11 and p9.13"
        sudo config-pin P9.11 uart
        sudo config-pin -q P9.11
        sudo config-pin P9.13 uart
        sudo config-pin -q P9.13
        echo -e "\n UART 1 configuration p9.26 and p9.24"
        sudo config-pin P9.24 uart
        sudo config-pin -q P9.24
        sudo config-pin P9.26 uart
        sudo config-pin -q P9.26
        echo -e "\n UART 5 configuration p8.38 and p8.37"
        sudo config-pin P8.38 uart
        sudo config-pin -q P8.38
        sudo config-pin P8.37 uart
        sudo config-pin -q P8.37
        echo -e "\n UART configuration end" 
else    
        echo "Oops!!configuration is not available"
        echo "Please check uEnv.txt file and only disable HDMI"
fi
