"""
Executable MicroPython Code:

Load into microcontroller as:
HwM_E4.py => main.py

Powered by YAKOTT
"""


"""
WT32-ETH01 v1.4
LAN Address Spoofing Attack

https://docs.micropython.org/en/latest/library/network.html
https://mpython.readthedocs.io/en/latest/library/micropython/network.html

Prompt: Write a script in MicroPython to connect to a LAN with a WT32-ETH01. Change the MAC address of the WT32-ETH01. Change the IP address of the WT32-ETH01.
"""


"""
Erase & Write Firmware

USB     WT32
5V  =>  5V
GND =>  GND
TX  =>  RX0
RX  =>  TX0
GND =>  IO0
"""


"""
Run

USB     WT32
5V  =>  5V
GND =>  GND
TX  =>  RX0
RX  =>  TX0
"""


# Packages


# Modules
# Machine
import machine
# Network
import network
# uBinaASCII
import ubinascii as binascii
# Time
import utime as time


# Global variables
# Wait time in seconds
wait_time_s = 1


# Functions


# Classes


# Main
print("LAN Address Spoofing Attack")
print()

# LAN() => Instantiate a network interface object
#   parameter
#       mdc => Set the mdc pin
#       mdio => Set the mdio pin
#       power => Set the pin which switches the power of the PHY device
#       phy_type => Select the PHY device type
#       phy_addr => Address number of the PHY device
#       ref_clk_mode => Data clock is provided by the Ethernet controller (True) or the PYH interface (False)
#       ref_clk => Defines the Pin used for ref_clk
station = network.LAN(mdc=machine.Pin(23), mdio=machine.Pin(18), power=machine.Pin(16), phy_type=network.PHY_LAN8720, phy_addr=1)

# Turn on LAN
print("Turn on LAN")
# active() => Activate/Deactivate the networt interface
#   True => Activate
#   False => Deactivate
station.active(True)
print()

print("Device Information")
# decode() => Encodes the string to bytes using UTF-8 by default
# hexlify() => Return the hexadecimal representation of the binary data
# config() => Get/Set general network interface parameters
#   parameter => Standar IP configuration
#       mac/'mac' => Only MAC address
print("  MAC Address: " + binascii.hexlify(station.config('mac'), ':').decode())
# hostname() => Get or set the hostname that will identify this device on the network
#   parameter
#       name => Hostname
print("  Hostname: " + network.hostname())
# country() => Get or set the two-letter ISO 3166-1 Alpha-2 country code to be used for radio compliance
#   parameter
#       code => "EC"
print("  Country: " + network.country())
print()

print("New Device Information")
# https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
# Apple, Inc.           18F643000001    Brian's iPhone
# Cisco Systems, Inc    18E728000001    router
mac_hexadecimal = "18F643000001"
# unhexlify() => Return the binary data representation by the hexadecimal string
mac_binary = binascii.unhexlify(mac_hexadecimal)
# config() => Get/Set general network interface parameters
#   parameter => Standar IP configuration
#       mac/'mac' => BSSID MAC address
station.config(mac=mac_binary)
network.hostname("Unknown")
network.country("EC")
#network.phy_mode(network.MODE_11G))
print("  MAC Address: " + binascii.hexlify(station.config('mac'), ':').decode())
print("  Hostname: " + network.hostname())
print("  Country: " + network.country())
print()

print("Connecting ",end="")
for j in range (0, 60, 1):
    print(".", end="")
    # isconnected() => Confirm is the network interface is connected to a LAN network
    if(station.isconnected()):
        break
    # sleep() => Wait time in seconds
    time.sleep(wait_time_s)
print()
state_option = ["No connected", "Connected"]
state_value = station.isconnected()
state = state_option[state_value]
print(state)
print()

print("Status")
for j in range (0, 60, 1):
    print(".", end="")
    if(station.status() == 5):
        break
    # sleep() => Wait time in seconds
    time.sleep(wait_time_s)
print()
# status() => Query dynamic information of the network interface
#   response
#       1 => STAT_IDLE
#       2 => STAT_CONNECTING
#       3 => STAT_WRONG_PASSWORD
#       4 => STAT_NO_AP_FOUND
#       5 => STAT_GOT_IP
#       6 => STAT_ASSOC_FAIL
#       7 => STAT_BEACON_TIMEOUT
#       8 => STAT_HANDSHAKE_TIMEOUT
response_option = {"1": "STAT_IDLE", "2": "STAT_CONNECTING", "3": "STAT_WRONG_PASSWORD", "4": "STAT_NO_AP_FOUND", "5": "STAT_GOT_IP", "6": "STAT_ASSOC_FAIL", "7": "STAT_BEACON_TIMEOUT", "8": "STAT_HANDSHAKE_TIMEOUT"}
response_value = station.status()
print(" ", response_option[str(response_value)])
print()

print("IP Information:")
# ifconfig() => Get/Set IP-level network interface parameters
#   ip => IP address
#   subnet_mask => Subnet mask
#   gateway => Gateway
#   dns_server => DNS server
print("  IP Address: " + station.ifconfig()[0])
print("  Subnet Mask: " + station.ifconfig()[1])
print("  IP Gateway: " + station.ifconfig()[2])
print("  DNS Server: " + station.ifconfig()[3])
print()

print("New IP Information:")
ip = "192.168.0.28"
subnet_mask = station.ifconfig()[1]
gateway = station.ifconfig()[2]
dns_server = station.ifconfig()[3]
station.ifconfig((ip, subnet_mask, gateway, dns_server))
print("  IP Address: " + station.ifconfig()[0])
print("  Subnet Mask: " + station.ifconfig()[1])
print("  IP Gateway: " + station.ifconfig()[2])
print("  DNS Server: " + station.ifconfig()[3])
print()

# Turn off LAN
print("Turn off LAN")
print()
station.active(False)
