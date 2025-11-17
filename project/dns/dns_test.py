import pytest
import subprocess

def test_nameserver():
    correct_nameserver = "10.0.0.2"

    result = subprocess.check_output(f"cat /etc/resolv.conf",
                            text=True,
                            shell=True
                        ).strip()
    
    assert result == correct_nameserver

    
    
#Bind 9

def test_bind9_is_active():
    result = subprocess.run(f'systemctl status bind9 | grep "active (running)"', check=True, capture_output=True, shell=True)    

    assert result.returncode == 0;

def test_bind9_correct_port():
    result = subprocess.run(f'ss -tulpn | grep :53', check=True, capture_output=True, shell=True)    

    assert result.returncode == 0;

def test_bind9_syntax():
    result = subprocess.run(f'named-checkconf', check=True, capture_output=True, shell=True)    

    assert result.returncode == 0;

def test_forward_zone():
    result = subprocess.run(f'named-checkzone mainzone.lab /etc/bind/db.mainzone.lab', check=True, capture_output=True, shell=True)    

    assert result.returncode == 0;
    
def test_reverse_zone():
    result = subprocess.run(f'named-checkzone 0.0.10.in-addr.arpa /etc/bind/db.10.0.0', check=True, capture_output=True, shell=True)    

    assert result.returncode == 0;