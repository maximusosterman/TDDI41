#!/usr/bin/env python3
import subprocess
import pwd


def test_root_exists():
    result = subprocess.run(
        ["getent", "passwd", "root"], capture_output=True, text=True
    )
    assert bool(result.stdout.strip())


def test_games_has_no_shell():
    shell = pwd.getpwnam("games").pw_shell
    assert shell in ["/usr/sbin/nologin", "/bin/false"]


def main():
    test_root_exists()
    test_games_has_no_shell()


if __name__ == "__main__":
    main()
