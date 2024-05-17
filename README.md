
# Overview
**OneShot** performs [Pixie Dust attack](https://forums.kali.org/showthread.php?24286-WPS-Pixie-Dust-Attack-Offline-WPS-Attack) without having to switch to monitor mode.
# Features
 - [Pixie Dust attack](https://forums.kali.org/showthread.php?24286-WPS-Pixie-Dust-Attack-Offline-WPS-Attack);
 - integrated [3WiFi offline WPS PIN generator](https://3wifi.stascorp.com/wpspin);
 - [online WPS bruteforce](https://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf);
 - Wi-Fi scanner with highlighting based on iw;
# Requirements
 - Python 3.6 and above;
 - [Wpa supplicant](https://www.w1.fi/wpa_supplicant/);
 - [Pixiewps](https://github.com/wiire-a/pixiewps);
 - [iw](https://wireless.wiki.kernel.org/en/users/documentation/iw).
# Setup
## Debian/Ubuntu
**Installing requirements**
 ```
 sudo apt install -y python3 wpasupplicant iw wget
 ```
**Installing Pixiewps**

***Ubuntu 18.04 and above or Debian 10 and above***
 ```
 sudo apt install -y pixiewps
 ```
 

**Getting OneShot**
 ```
 cd ~
 wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/cyb3rgh0st.py
 ```
Optional: getting a list of vulnerable to pixie dust devices for highlighting in scan results:
 ```
 wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/vulnwsc.txt
 ```
## Arch Linux
**Installing requirements**
 ```
 sudo pacman -S wpa_supplicant pixiewps wget python
 ```
**Getting OneShot**
 ```
 wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/cyb3rgh0st.py
 ```
Optional: getting a list of vulnerable to pixie dust devices for highlighting in scan results:
 ```
 wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/vulnwsc.txt
 ```

 **Getting OneShot**
 ```
 sudo wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/cyb3rgh0st.py
 ```
Optional: getting a list of vulnerable to pixie dust devices for highlighting in scan results:
 ```
 sudo wget https://raw.githubusercontent.com/Mr-Cyb3rgh0st/wifi-hacking/main/vulnwsc.txt
 ```
## [Termux](https://termux.com/)
Please note that root access is required.  

#### Manually
**Installing requirements**
 ```
 pkg install -y root-repo
 pkg install -y git tsu python wpa-supplicant pixiewps iw openssl
 ```
**Getting OneShot**
 ```
 git clone https://github.com/Mr-Cyb3rgh0st/wifi-hacking
 ```
#### Running
 ```
 python main.py
 ```


## Troubleshooting
#### "RTNETLINK answers: Operation not possible due to RF-kill"
 Just run:
```sudo rfkill unblock wifi```
#### "Device or resource busy (-16)"
 Try disabling Wi-Fi in the system settings and kill the Network manager. Alternatively, you can try running OneShot with ```--iface-down``` argument.
#### The wlan0 interface disappears when Wi-Fi is disabled on Android devices with MediaTek SoC
 Try running OneShot with the `--mtk-wifi` flag to initialize Wi-Fi device driver.
# Acknowledgements


## Modify

`Mr. Cyb3rgh0st`

