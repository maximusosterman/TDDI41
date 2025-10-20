## Shebang - [SCT.1](https://www.ida.liu.se/~TDDI41/2025/uppgifter/sct/index.sv.shtml#SCT.1)
En shebang fungerar som tolk för unix när den ska köra filer. Unix kollar inte på filendelser, därför kan man föutse datorn med information om vad som behövs för att köra filen. För python exempelvis: "#!/usr/bin/env python3" detta resulterar i att man kan köra pyhonscriptet i terminalen med ./filnamn.py

## Skript för att automatiskt skapa användarkonto - [SCT.2](https://www.ida.liu.se/~TDDI41/2025/uppgifter/sct/index.sv.shtml#SCT.2)
``` python
#!/usr/bin/env python3
import sys
import subprocess
import random
import string
import unicodedata
import argparse
from pathlib import Path


class UserAddError(Exception):
    pass

class UserAlreadyExists(UserAddError):
    pass

class PasswordChangeError(Exception):
    pass

Exception

def user_exists(user: str) -> bool:
    result = subprocess.run(
        ["getent", "passwd", user], capture_output=True, text=True
    )
    return  bool(result.stdout.strip())


def generate_liuid(name: str, lastname: str) -> str:
    return (name[:3] + lastname[:2]).lower() + str(random.randint(100, 999))


def normalize_name(s: str) -> str:
    """Normalize to lowercase a-z only, mapping å/ä/ö → a."""
    # Normalize to NFKD (decompose accents)
    s = unicodedata.normalize("NFKD", s)

    # Replace Swedish letters manually first
    s = (
        s.replace("å", "a").replace("Å", "A")
         .replace("ä", "a").replace("Ä", "A")
         .replace("ö", "o").replace("Ö", "O")
    )

    # Encode to ASCII (dropping other diacritics), decode back
    s = s.encode("ascii", "ignore").decode("ascii")

    # Keep only letters and lowercase
    return "".join(ch for ch in s.lower() if ch.isalpha())


def make_safe_string(name: str, lastname: str) -> tuple[str, str]:
    # normalize
    name = normalize_name(name)
    lastname = normalize_name(lastname)

    # pad to required length
    if len(name) < 3:
        name += "".join(random.choice(string.ascii_lowercase)
                        for _ in range(3 - len(name)))
    if len(lastname) < 2:
        lastname += "".join(random.choice(string.ascii_lowercase)
                            for _ in range(2 - len(lastname)))

    return name, lastname


def get_liuid(fullname: str) -> str:

    try:
        name, lastname = fullname.split(" ")

    except:
        splitted_fullname = fullname.split(" ")
        name = splitted_fullname[0]
        lastname = splitted_fullname[-1]

    safe_name, safe_lastname = make_safe_string(name, lastname)

    while True:

        try:
            liuid = generate_liuid(safe_name, safe_lastname)
            if not user_exists(liuid):
                break

        except:
            liuid = generate_liuid(safe_name, safe_lastname)


    return liuid


def generate_password() -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(8))


def create_user(liuid: str, password: str, dry_run: bool = False) -> None:

    if dry_run:
            print(f"[DRY-RUN] useradd -m -s /bin/bash {liuid}")
            print(f"[DRY-RUN] echo '{liuid}:{password}' | chpasswd")
            return
        
    # Addning user
    result = subprocess.run(
        ["useradd", "-m", "-s", "/bin/bash", liuid],
        capture_output=True,
        check=True
    )
    
    if result.returncode != 0:
        stderr = result.stderr.strip()
        if "already exists" in stderr:
            raise UserAlreadyExists(stderr)
        else:
            raise UserAddError(stderr)

    # Password change
    result = subprocess.run(
        ["chpasswd"],
        input=f"{liuid}:{password}\n",
        text=True, 
        check=True
    )

    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise PasswordChangeError(stderr)

    return

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Create Linux users from a list of names.")
    p.add_argument("file", type=Path, help="Path to a UTF-8 text file with one full name per line.")
    p.add_argument("--dry-run", action="store_true", help="Do not execute useradd/chpasswd; just print actions.")
    return p.parse_args()


def main():

    args = parse_args()

    confirm = False

    while not confirm and not args.dry_run:
        print("WARNING: This script is NOT being run with --dry-run flag and will create acutal users in your system!")
        user_in = input("Are you sure you want to proceed? [y/n]: ")
        if user_in.lower() in ["y", "yes"]:
            confirm = True

        elif user_in.lower() in ["n", "no"]:
            sys.exit(0)

        else:
            print("Not valid input!")

    if not args.file.exists():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8", errors="replace") as file:
        list_of_names = file.readlines()

        for name in list_of_names:
            name = name.strip()
            if not name:
                print("Empty name!")
                continue

            liuid = get_liuid(name)
            password = generate_password()


            while True:
                try:
                    create_user(liuid, password, args.dry_run)
                    print("Input name: " + name)
                    print(f"User created! -> {liuid} | Password: {password}\n")
                    break

                except UserAlreadyExists:
                    print(f"{liuid} already exits! Generating a new one, trying again...")
                    liuid = get_liuid(name)

                except UserAddError as e:
                    print(f"Unexcpected error! Failed to create {liuid}: {e}")
                    break

                except PasswordChangeError as e:
                    print(f"Unexpected error! Failed to change password {liuid}: {e}")
                    break

            

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
