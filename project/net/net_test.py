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

def test_can_reach_router():

    router_ip = "10.0.0.1"

    result = subprocess.run(f"ping -c 1 -w 5 {router_ip}",
                   check=True,
                   capture_output=True,
                   shell=True
                )
    
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

    correct_gateway = "dev"

    result = subprocess.check_output("ip route",
                                    text=True,
                                    shell=True     
                                )

    assert correct_gateway in result

def main():
    test_correct_ip()
    test_correct_netmask()
    test_correct_gateway()
    
    test_name()
    
    test_can_reach_router()

if __name__ == "__main__":
    main()  