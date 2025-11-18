import pytest
import subprocess

CURR_IP     = "10.0.0.3"
CURR_NAME   = "client-1"
SERVER_IP   = "10.0.0.2"
ZONE_NAME    = "mainzone.lab"

def test_nameserver_soa():
    result = subprocess.check_output(
        f"dig @{SERVER_IP} {ZONE_NAME} SOA +noall +answer +time=1 +tries=1",
        text=True,
        shell=True
    ).strip()

    assert ZONE_NAME in result
    assert "SOA" in result
    assert f"ns1.{ZONE_NAME}" in result


def test_bind9_is_active():
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", "bind9"],
        check=False
    )

    assert result.returncode == 0

def test_strict_dns_listen():
    result = subprocess.run(
        ["ss", "-tulpn", "sport = :53"],
        capture_output=True,
        text=True
    )
    stdout = result.stdout

    assert f"{SERVER_IP}:53" in stdout
    assert "named" in stdout

def dig(name, server=None):
    cmd: list[str] = ["dig", "+noall", "+answer"]
    if server:
        cmd.insert(1, f"@{server}")
    cmd.append(name)
    return subprocess.run(cmd, capture_output=True, text=True, check=False)

def test_zone_has_correct_records():
    res = dig(f"{CURR_NAME}.{ZONE_NAME}", SERVER_IP)

    assert SERVER_IP in res.stdout

def test_zone_is_authoritative():
    res = subprocess.run(
        ["dig", f"@{SERVER_IP}", ZONE_NAME, "SOA", "+cmd"],
        capture_output=True,
        text=True
    )
    assert "SOA" in res.stdout
    assert " aa," in res.stdout or " aa " in res.stdout

def test_external_resolution_via_forwarder():
    res = subprocess.run(
        ["dig", f"@{SERVER_IP}", "www.ida.liu.se", "+short"],
        capture_output=True,
        text=True
    )
    
    assert res.stdout.strip() != "", "External resolution failed via forwarder"

def test_client1_uses_internal_dns():
    res = subprocess.run(
        ["dig", "www.ida.liu.se"],
        capture_output=True,
        text=True
    )

    # dig skriver ut vilken DNS-server som används i CMD-delen
    assert f"SERVER: {SERVER_IP}#53" in res.stdout, \
        "Client-1 is not using internal DNS server"
    
def test_reverse_dns():
    res = subprocess.run(["dig", f"@{SERVER_IP}", "-x", CURR_IP, "+short"],
        capture_output=True, text=True)
    assert f"server.{ZONE_NAME}." in res.stdout