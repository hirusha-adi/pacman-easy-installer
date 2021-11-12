import os
import platform


def pacman_make_ready():
    os.system("pacman -Syy --noconfirm")
    os.system("pacman -Syu --noconfirm")


def pacman_fix_common_error():
    os.system("sudo pacman-mirrors -f && sudo pacman -Syyuu")


def pacman_install(package_name: str = None):
    if package_name is None:
        print("+ Please enter the package name")
    os.system(f"pacman -S {package_name.lower()} --noconfirm")


def install_all_for_mainrig():
    """
    Should i run these? or should i keep the zen kernel
        sudo pacman -S linux-lts
        sudo pacman -S linux-lts-headers
    """
    pacman_make_ready()
    all_packages = [
        "base-devel", "git", "atom", "audacious", "audacity",
        "eclipse-java", "firefox", "flameshot", "gimp", "kate",
        "github-desktop",  "kdenlive", "nano", "vim", "neofetch",
        "netbeans", "nmap", "obs-studio", "pamac-aur", "qbittorrent",
        "pycharm-community-edition", "python-pip", "snapd", "spotify-adblock-git",
        "sublime-text-4", "steam", "sudo", "teams", "teamviewer",
        "telegram-desktop", "tor-browser", "tk", "vlc", "wget",
        "wps-office", "woeusb-gui", "yakuake", "yay", "zoom",
        "bpytop", "htop", "ffpmeg", "partitionmanager", "curl",
        "discord", "bitwarden", "gedit", "jellyfin-media-player"
        "p7zip", "p7zip-plugins", "unrar", "tar", "rsync", "snapd"
    ]
    for package in all_packages:
        pacman_install(package_name=package)


def ENTIRE_PROGRAM():
    print(f""" 
                  _                          
    __      _____| | ___ ___  _ __ ___   ___ 
    \ \ /\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\
     \ V  V /  __/ | (_| (_) | | | | | |  __/
      \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

            * Node: {platform.uname().node}
            * System: {platform.uname().system}
            * Kernel: {platform.release()}
            * Machine: {platform.machine()}
    """)
    print(""" 
             [1] MainRig
    """)
    mmo = input("? Please select and option: ")
    if mmo == "1":
        os.system("clear")
        print(r"""
  _     _                _             ____  __  __       _       ____  _       
 | |__ (_)_ __ _   _ ___| |__   __ _  / __ \|  \/  | __ _(_)_ __ |  _ \(_) __ _ 
 | '_ \| | '__| | | / __| '_ \ / _` |/ / _` | |\/| |/ _` | | '_ \| |_) | |/ _` |
 | | | | | |  | |_| \__ \ | | | (_| | | (_| | |  | | (_| | | | | |  _ <| | (_| |
 |_| |_|_|_|   \__,_|___/_| |_|\__,_|\ \__,_|_|  |_|\__,_|_|_| |_|_| \_\_|\__, |
                                      \____/                              |___/ 
    
     + You will be installing the packages listed below
        """)
        print("""        atom, audacious, audacity, bitwarden, discord,
        eclipse-java, firefox, flameshot, gimp, kate
        github-desktop, kdenlive, nano, vim, neofetch
        netbeans, nmap, obs-studio,amacaur, qbittorrent
        pycharm-community-edition, python-pip, snapd, 
        spotify-dblockgit, partitionmanager, ffpmeg, 
        sublime-text-4,steam, sudo, teams, teamviewer
        telegram-desktop, tor-browser, tk, vlc, wget
        wps-office, woeusb-gui, yakuake, yay, zoom
        bpytop, htop, curl, snapd, jellyfin-media-player
             """)
        smo1 = input("? Hit enter if you want to continue: ")
        if smo1.lower().startswith("q"):
            exit()
        install_all_for_mainrig()


if __name__ == "__main__":
    ENTIRE_PROGRAM()
