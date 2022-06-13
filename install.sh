sudo apt install git -y
cd /opt
sudo git clone https://github.com/stepanyuk-aa/waterDrone.git
cd waterDrone/src
sudo apt install python3
sudo apt install python3-pip -y

sudo pip3 install pymysql
sudo pip3 install gps
sudo pip3 install flask
sudo pip3 install flask_cors
sudo pip3 install pigpio

sudo apt install mariadb-server -y
sudo sed -i "s/bind-address            = 127.0.0.1/bind-address            = 0.0.0.0/" /etc/mysql/mariadb.conf.d/50-server.cnf
sudo mysql -u root < /opt/waterDrone/db.sql

sudo apt install hostapd dnsmasq -y
echo "interface=wlan0
dhcp-range=192.168.10.10,192.168.10.100,255.255.255.0,24h
domain=water.drone" >> /etc/dnsmasq.conf

echo "	country_code=RU
interface=wlan0
ssid=WaterDrone
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=123456789
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf

sudo systemctl restart dhcpcd.service
sudo systemctl restart dnsmasq
sudo systemctl restart hostapd
