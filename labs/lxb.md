

## Introduktion till <code>man</code> - [LXB.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.1)

#### Vilka är de 9 avsnitten?
1   Executable programs or shell commands
2   System calls (functions provided by the kernel)
3   Library calls (functions within program libraries)
4   Special files (usually found in /dev)
5   File formats and conventions, e.g. /etc/passwd
6   Games
7   Miscellaneous  (including  macro  packages  and  conventions),  e.g. man(7), groff(7),
    man-pages(7)
8   System administration commands (usually only for root)
9   Kernel routines [Non standard]

#### Vilket avsnitt dokumenterar kommandoradsverktyg så som <code>cat</code> eller <code>ls</code>?

<code>cat</code> och <code>ls</code> finns båda dokumenterade i sektion 1

#### Introduktion till rör [LXB.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.2)

maxve266@su24-213:~/dev$ journalctl | tail --lines=5
Hint: You are currently not seeing messages from other users and the system.
      Users in groups 'adm', 'systemd-journal' can see all messages.
      Pass -q to turn off this notice.
sep 11 11:25:14 su24-213.ad.liu.se vsce-sign[470984]: Exit code:  Success
sep 11 11:28:52 su24-213.ad.liu.se systemd[435157]: Started Common interface to speech synthesizers.
sep 11 11:28:52 su24-213.ad.liu.se speech-dispatcher[476947]: [Thu Sep 11 11:28:52 2025 : 92297] speechd: Speech Dispatcher 0.11.1 starting
sep 11 11:33:57 su24-213.ad.liu.se systemd[435157]: Starting Warn the user if their home directory is dangerously full....
sep 11 11:33:57 su24-213.ad.liu.se systemd[435157]: Finished Warn the user if their home directory is dangerously full..


#### Justering av filrättigheter - [LXB.3](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.3)
Man ändrar ägare med hjälp av kommandot <code>chown newuser filname</code>

Forsättningsvis för att göra filen exekverbar för endast en grupp måste man ta bort
rättigheter för ägare, och övriga. Rättigheterna ska endast tilldelas gruppen.
Detta gör man med kommandot chmod och sedan anger parametrar 070 och filnamn


#### Arkivering och komprimering med <em>tarballs</em> - [LXB.4](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.4)

<code>tar -xvzf filnamn.tar.gz </code> för att packa upp innehållet
<code>tar -cvzf filnamn.tar.gz </code> för att packa ner innehållet

Skillanden mellan dessa flaggan x och c som står för eXtract och Create


#### Miljövariabler - [LXB.5](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.5)


Vi använde echo för att skriva utt i terminalen vilket gav utskriften "Hej maxve266". Sedan lade vi till pathen till courses/TDDI42 vilken möjligjorde exikvering av scriptet start_single.sh som öppnade VM:en. Därefter gick vi in i bashrc och gjorde pathen "global" vilket gör så att skriptet är åtkommligt från alla directories. LC_ALL bytte språk på man(1) till svenska.


#### Introduktion till <code> systemd </code>- [LXB.6](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.6)

Kommandot för att få en lista över alla systemenheter skrivs <code>systemctl list-units --all</code>. För att starta om ssh-server skriver man <code>sudo systemctl restart ssh</code>.

#### Systemloggar - [LXB.7](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.7)

root@debian:~# journalctl -u sshd
-- Journal begins at Mon 2022-06-27 16:24:57 CEST, ends at Thu 2025-09-11 12:55:59 CEST. --
-- No entries --

#### SSH-nycklar för autentisering - [LXB.8](https://www.ida.liu.se/~TDDI41/2025/uppgifter/lxb/index.sv.shtml#lxb.8)

Började med att skapa en ssh-nyckel på hosten. Därefter även skapa en på VMen. Ange namn på nycklar med flaggan -C och -t för rätt ssh-algoritm.

Därefter kopiera sin public key på hosten och lägga in den i authorized keys på VMen. Detta kan göras med komandot ssh-copy-id

Exakta loggar från terminalen fanns inte tillgängliga i en smidig visning.





