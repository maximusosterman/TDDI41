import pytest
import subprocess

def test_name():

    current_host = "vippan-107.ad.liu.se"

    result = subprocess.run(f"hostname | grep {current_host}",
                check=True,
                capture_output=True,
                shell=True
            )
    
    assert result.returncode == 0

def test_can_reach():

    ip_list = ["google.com", "10.0.2.2"]

    for ip in ip_list:
        result = subprocess.run(f"ping -c 1 -w 5 {ip}", check=True, capture_output=True, shell=True)
        assert result.returncode == 0

def test_correct_ip():

    correct_ip = "10.0.0.1"

    result = subprocess.check_output(f"hostname -i",
                            text=True,
                            shell=True
                        ).strip()
    
    assert result == correct_ip

def test_correct_netmask():

    correct_netmask = "24"

    result = subprocess.check_output("ip addr show dev ens3 | grep inet -m 1 | awk '{print $2}'",
                                    text=True,
                                    shell=True
                                )

    assert result.split("/")[1].strip() == correct_netmask

def test_correct_gateway():

    correct_gateway = "10.0.0.1"

    result = subprocess.check_output("ip route",
                                    text=True,
                                    shell=True     
                                )

    assert correct_gateway in result

def test_if_ip_forwarding_enabled():
    result = subprocess.check_output("cat /proc/sys/net/ipv4/ip_forward",
                                    text=True,
                                    shell=True     
                                ).strip()
    
    assert result == "1"

def test_masquerading():
    result = subprocess.run("nft list ruleset", check=True, capture_output=True, shell=True, text=True)

    assert 'oifname "ens3" masquerade' in result.stdout.strip()
    


def main():
    test_correct_ip()
    test_correct_netmask()
    test_correct_gateway()
    
    test_name()
    
    test_can_reach()

    test_if_ip_forwarding_enabled()

    test_masquerading()

if __name__ == "__main__":
    main()  