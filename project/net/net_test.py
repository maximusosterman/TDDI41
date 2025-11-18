import pytest
import subprocess
import netifaces as ni

ROUTER_IP = "10.0.0.1"
CURR_HOSTNAME = "client-1"
CURR_IP = "10.0.0.3"
NETMASK = "255.255.255.0"
INTERFACE_NAME = "ens3"
SSH_PORT = "22"

def test_name():

    result = subprocess.run(f"hostname | grep {CURR_HOSTNAME}",
                check=True,
                capture_output=True,
                shell=True
            )
    
    assert result.returncode == 0

def test_can_reach_router():

    result = subprocess.run(f"ping -c 1 -w 5 {ROUTER_IP}",
                   check=True,
                   capture_output=True,
                   shell=True
                )
    
    assert result.returncode == 0


def test_can_reach():

    ip_list = ["google.com", "10.0.2.2", CURR_IP, "10.0.0.3"]

    for ip in ip_list:
        if CURR_IP == ip : continue 
        result = subprocess.run(f"ping -c 1 -w 5 {ip}", check=True, capture_output=True, shell=True)
        assert result.returncode == 0


def get_ip(iface):
    return ni.ifaddresses(iface)[ni.AF_INET][0]['addr']


def get_netmask(iface):
    return ni.ifaddresses(iface)[ni.AF_INET][0]['netmask']
        
def test_correct_ip():
    assert CURR_IP == get_ip(INTERFACE_NAME)

def test_correct_netmask():
    assert NETMASK == get_netmask(INTERFACE_NAME)


def test_correct_gateway():

    correct_gateway = "10.0.0.0"

    result = subprocess.check_output("ip route",
                                    text=True,
                                    shell=True     
                                )

    assert correct_gateway in result

def test_icmp_inbound_to_client1():
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "3", "10.0.0.3"],
        capture_output=True
    )
    assert result.returncode == 0

def test_client1_ssh_port_open():
    result = subprocess.run(f"nc -vz {CURR_IP} {SSH_PORT}", capture_output=True, shell=True)

    assert result.returncode == 0 

 

