import subprocess
import os

def post_install():
    # Compile dconf database
    subprocess.run(["dconf", "update"], check=True)

    # Flathub remote
    subprocess.run([
        "flatpak", "remote-add", "--if-not-exists", "flathub",
        "https://dl.flathub.org/repo/flathub.flatpakrepo"
    ])
