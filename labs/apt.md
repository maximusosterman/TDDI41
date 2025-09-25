## Pakethantering - [APT.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/apt/index.sv.shtml#apt.1)
<code>apt install </code> <br>
<code>apt remove </code> <br>
<code>apt purge </code> <br>
<code>apt list </code> <br>
<code>apt upgarde </code> <br>



## Pakethantering, forts. - [APT.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/apt/index.sv.shtml#apt.2)

1. <code>dpkg -L</code> <br>
2. <code>dpkg -S /Sökväg/till/fil</code>
<br>
kör man kommandot på VM:en får man att filen toillhör paketet "perl".

## Paketinstallation  - [APT.3](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.3)

1. <code>apt install cowsay</code>


2. root@debian:~# /usr/games/cowsay hej
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = "en_US:en",
	LC_ALL = (unset),
	LC_ADDRESS = "sv_SE.UTF-8",
	LC_NAME = "sv_SE.UTF-8",
	LC_MONETARY = "sv_SE.UTF-8",
	LC_PAPER = "sv_SE.UTF-8",
	LC_IDENTIFICATION = "sv_SE.UTF-8",
	LC_TELEPHONE = "sv_SE.UTF-8",
	LC_MESSAGES = "en_GB.UTF-8",
	LC_MEASUREMENT = "sv_SE.UTF-8",
	LC_CTYPE = "sv_SE.UTF-8",
	LC_TIME = "sv_SE.UTF-8",
	LC_COLLATE = "sv_SE.UTF-8",
	LC_NUMERIC = "sv_SE.UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
 _____
< hej >
 -----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

3. <code> apt purge cowsay -> y </code>

## *Repository*-hantering  - [APT.4](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.4)

1. Vi börjarde med att installera curl via apt. Därfer <br>
``` bash
#Add the release PGP keys: 

mkdir -p /etc/apt/keyrings <br>
curl -L -o /etc/apt/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg

#Add the "stable-v2" channel to your APT sources:
echo "deb [signed-by=/etc/apt/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable-v2" | sudo tee /etc/apt/sources.list.d/syncthing.list

# Add the "candidate" channel to your APT sources:
echo "deb [signed-by=/etc/apt/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing candidate" | sudo tee /etc/apt/sources.list.d/syncthing.list

# Update and install syncthing:
sudo apt-get update
sudo apt-get install syncthing
```


2. 
```bash
rm /etc/apt/sources.list.d/syncthing.list 
```