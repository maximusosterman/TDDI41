## <code>Grunderna i DNS</code> - [DNS.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/dns/#dns.1)

1. Det är en DNS server som har svaret för alla maskiner och domännamn. 
2. Rekursiv namnserver
3. Ett domän är ett namn i DNS-hierarkin medan en zon innehåller poster inom sitt områdede. Ett domän kan innehålla flera zoner medan en zon alltid innehåller ett domän.
4. Du ställer samma svar till flera servar för att få ett giltigt svar. Server letar upp svaret åt klienten. Iterativ slagning är när du själv stegar igenom servrar för att hitta rätt auktoritiv server. Med hjälp av RD-flaggan kan du göra frågan rekursiv. 
5. Det ska bli skalbart och varje zon kan då styras av olika personer vilket gör det flexibelt.
6. Det gör man via Reverse DNS vilket gör ip-adress -> domännamn via PTR-post. 

## <code>dig</code> - [DNS.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/dns/#dns.2)

dig www.liu.se skickar en fråga till DNS "vad är ip:n för www.liu.se?"
Som svar får man tillbaka vilken ip domänen är på.
Dessutom får man även en summering på vad man har skickat  mer för queries, hur långt tid requesten tog och när den ägde rum. 

2. 
- A ska innehålla domän namn i IPv4-address
- AAAA är samma fast för IPv6
- MX innehåkker Mail Exchange
- NS innehåller Name servers för zonen
- SOA innehåller metadata för hela zoenen

3. Med +trace plus använder man sig av manuell rekursion. Man får ta del av varje steg. Från Rootservar till att man hittar ip:n för google. Man får se vilka NS som hanterar .com, sen från alla .com till alla googles servar där man hittar slutgiltiga ip:n


## <code>dig</code> - [DNS.3](https://www.ida.liu.se/~TDDI41/2025/uppgifter/dns/#dns.3)
1. vi sätter upp vår DNS-server till google:s offentliga DNS-server eftersom den är snabb, stabil och gratis att använda. Detta görs genom att lägga till raden "dns-nameservers " i vår 
/etc/network/interfaces fil på servern och clientena.  

2. En SOA-post beskriver vem som ansvarar för zonen och hur den ska synkas till primära och sekundära namnservrar. De olika fälten är:

- Primära NS: zonens master-server. 
- Responsible person: Kontakt-adress. 
- Serial: Verisionsnummer för zonen.
- Refresh: Hur ofta sekundärer frågar efter uppdateringar
- Retry: Hur ofta sekundärer försöker igen vid nätverksproblem
- Expire: hur länge sekundäerer får användad gammal zon innan allt stängs
- minimum TTL: 

För att sätta upp egen auktoritet för vår zon hämtade vi bind9 på clienterna och servern. Därefer skapade vi filen mainzone.db som ligger i vår bind mapp. Vi satte upp vad zonen skulle ha för konfigrueringar (refresh, TTL, expire osv). För att alla maskinnamn skulle kunna kopplas till rätt ip modifierade vi filen named.conf.local där vi sätter mainzone.lab till master. Anakin(client-1) slicar mace windu(routern) och inser att palpatine(servern) är den sanna mästaren. 
- [Hur det utspelar sig ](https://www.youtube.com/watch?v=O8QSTzWhvG0&pp=ygUQbWFjZSB3aW5kdSBkaWVzIA%3D%3D)
- [hur client-1 beter sig](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3D6lg31YxfD7k&ved=2ahUKEwjd8b7e_fGQAxX7OBAIHT6wPKkQtwJ6BAgQEAI&usg=AOvVaw3Agi4TLfVyrmMqRV6vB9jj) 
- [serverns respons](https://www.youtube.com/watch?v=EzfkxAC-Bw8&pp=ygUOZ29vZCBwYWxwYXRpbmXSBwkJCAoBhyohjO8%3D)

Sedan gick vi in i filen named.conf.options där vi tillåter slagning, frågeställning, och att localhost och servern är masters och vi ska lyssna på dem. För att sätta upp reverse dns skapade vi filen db.10.0.0 och vi använder oss av ungeför samma konfigruering som i named.conf.options men lägger till PTR records som möjliggör för reverse dns för maskinernas ip-adresser. 

