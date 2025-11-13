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