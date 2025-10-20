## <code>ping</code> - [NET.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.1)

1. 
maxve266@su24-202:~/dev/TDDI41/project$ ping -c 5 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.094 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.067 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.074 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.071 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.080 ms
--- 127.0.0.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4092ms
rtt min/avg/max/mdev = 0.067/0.077/0.094/0.009 ms

2. 
maxve266@su24-202:~/dev/TDDI41/project$ ping -c 5 -i 2 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.090 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.051 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.034 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.041 ms
64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.083 ms

--- 127.0.0.1 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 8065ms
rtt min/avg/max/mdev = 0.034/0.059/0.090/0.022 ms


## <code>ip</code> - [NET.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.2)

1. ifconfig
2. ip links set ens4 up
3. ip addr add 192.168.1.2/24 dev ens4
4. ip route show



## Nätverkskonfiguration - [NET.3](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.3)

Vi började med att loggain på alla maskiner och öppna nano. Därefter satte vi upp ip-adresser, nätmask och gateway på varje maskin eligt nedan:

auto ens3
iface es3 inet static
    address 10.0.0.x
    netmask 255.255.255.0
    gateway 10.0.0.1 //samma som routern


Vi kollade m.h.a "systemctl restart networking" för att kolla så allt stämmde. Sedan testade vi att pinga maskinerna från alla maskiner och testade att skicka meddelanden från klienten till servern via att först öppna upp porten med kommandot "nc -lk -p 4444" och sedan ansluta med vår client med kommadot "nc 10.0.0.2 4444".


## *IP-forwarding och -masquerading* - [NET.4](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.4)

vi loggade in på vår gateway och öppnade nfttables.conf med nano och la till rulesetet: 

table inet nat {
    chain postrouting {
        type nat hook postrouting priority 100;
        oifname "ens3" masquerade
    }
}

detta möjligör att vi kan skicka paket från clienten genom routern till nätet. (vi kollade genom att pinga nätet från clienten)


## Justering av värdnamn - [NET.5](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.5)
Körde kommandot hostnamectl set-hostname client-1.grupp1337.liu.se 
Sedan editerade filen /etc/hosts med 
10.0.0.x    client-1.grupp1337.liu.se client 1

Starta sedan om med systemctl systemd-hostnamed
Validera med:
hostname
hostname -f
dnsdomainname

## Brandväggar med <code>nftables</code> - [NET.6](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.6)
Följande ändringar i /etc/nftabels.conf:
```conf
chain input {
        type filter hook input priority 0;

        # Utgår ifrån att all trafik ska släppas, utom den vi tillåter. - Deny by default   
        policy drop; 

        # Tillåter loopback. Används för att representera ett internt nätverk i datorn
        iifname "lo" accept 

        # Släpper igenom all trafik "som tillhör etablerade konversationer eller kopplingar, och relaterad trafik"
        ct state established,related accept 

        # Tillåter all icmp-trafik. Används för att kunna pinga t.ex
        ip protocol icmp accept

        #Tillåter ssh på port 22 
        ip protocol tcp tcp dport 22 accept
}

Allt detta gjordes på samtilga maskiner
```
[Source: drop](https://serverfault.com/questions/1187259/nftables-default-deny-but-allow-from-separate-tables)

[Source: Loopback](https://wiki.nftables.org/wiki-nftables/index.php/Simple_ruleset_for_a_server)

[Source: established,related & ICMP](https://bbs.archlinux.org/viewtopic.php?id=238422)

[Source: SSH](https://stackoverflow.com/questions/68622404/nftables-don%C2%B4t-allow-ssh)


## Testning av nätverkskonfiguration - [NET.7](https://www.ida.liu.se/~TDDI41/2025/uppgifter/net/index.sv.shtml#net.7)


