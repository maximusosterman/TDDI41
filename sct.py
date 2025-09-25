#!/usr/bin/env python3
import sys
import subprocess
import random
import string
import unicodedata

def user_exists(user):
    result = subprocess.run(
        ["getent", "passwd", user], capture_output=True, text=True
    )
    return  bool(result.stdout.strip())


def generate_liuid(name, lastname):
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

def make_safe_string(name, lastname):
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


def get_liuid(fullname):

    try:
        name, lastname = fullname.split(" ")

    except:
        splitted_fullname = fullname.split(" ")
        name = splitted_fullname[0]
        lastname = splitted_fullname[-1]

    print("Name: " + name + " " + lastname)

    name, lastname = make_safe_string(name, lastname)

    while True:
        liuid = generate_liuid(name, lastname)
        if not user_exists(liuid):
            break

    return liuid


def generate_password():
    return "".join(random.choice(string.ascii_letters) for _ in range(8))

def create_user(liuid):

    password = generate_password()

    subprocess.run(["useradd", "-m", "-s", "/bin/bash", liuid])
    subprocess.run(["chpasswd"], input=f"{liuid}:{password}\n", text=True, check=True)

    print("User created! -> " + liuid )
    print(f"Password for {liuid}: {password}\n")


def main():

    if len(sys.argv) < 2:
        print("Pleasr enter a list as argument!")
        sys.exit()

    with open(sys.argv[1], "r", encoding="utf-8", errors="replace") as file:
        list_of_names = file.readlines()

        for name in list_of_names:
            name = name.strip()
            if not name:
                print("Empty name!")
                continue

            liuid = get_liuid(name)
            create_user(liuid)


if __name__ == "__main__":
    main()
