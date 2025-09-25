## Shebang - [SCT.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/sct/index.sv.shtml#SCT.1)
En shebang fungerar som tolk för unix när den ska köra filer. Unix kollar inte på filendelser, därför kan man föutse datorn med information om vad som behövs för att köra filen. För python exempelvis: "#!/usr/bin/env python3" detta resulterar i att man kan köra pyhonscriptet i terminalen med ./filnamn.py

## Skript för att automatiskt skapa användarkonto - [SCT.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/sct/index.sv.shtml#SCT.2)
``` python
#!/usr/bin/env python3
import sys
import subprocess
import random
import string

def get_liuid():
    fullname_name = sys.argv[1]

    name, lastname = fullname_name.split('-')
    num = random.randint(100, 999)

    return name[:3] + lastname[:2] + str(num)

def generate_password():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))

def main():
    liuid = get_liuid()
    password = generate_password()

    subprocess.run(["useradd", "-m", "-s", "/bin/bash", liuid])
    subprocess.run(["chpasswd"], input=f"{liuid}:{password}\n", text=True, check=True)

    print("User created! ")
    print(f"Password for {liuid}: {password}")

if __name__ == "__main__":
    main()
```
## Skript för automatiserad testning - [SCT.3](https://www.ida.liu.se/~TDDI41/2025/uppgifter/sct/index.sv.shtml#SCT.3)

``` python
#!/usr/bin/env python3
import  subprocess
import pwd

def test_root_exists():

    #Fetch all users with "root" as filter
    result = subprocess.run(["getent", "passwd", "root"],  capture_output=True, text=True) 

    # If no output, it fails.
    assert bool(result.stdout.strip()) 

def test_games_has_no_shell():
    #Fetches all shells from user games
    shell = pwd.getpwnam("games").pw_shell

    #If games's shells are one of these, the test passes
    assert shell in ['/usr/sbin/nologin', '/bin/false']

def main():
    test_root_exists()
    test_games_has_no_shell()

if __name__ == "__main__":
    main()

```
