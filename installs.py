import os
import platform


def pacman_make_ready():
    os.system("pacman -Syy")
    os.system("pacman -Syu")


def pacman_fix_common_error():
    os.system("sudo pacman-mirrors -f && sudo pacman -Syyuu")


def pacman_install(package_name: str = None):
    if package_name is None:
        print("+ Please enter the package name")
    os.system(f"pacman -S {package_name.lower()}")


def install_for_me_custom():
    all_packages = [
        "atom", "audacious", "audacity", "bitwarden", "discord",
        "eclipse-java", "firefox", "flameshot", "gimp", "kate",
        "github-desktop",  "kdenlive", "nano", "vim", "neofetch",
        "netbeans", "nmap", "obs-studio", "pamac-aur", "qbittorrent",
        "pycharm-community-edition", "python-pip", "snapd", "spotify-adblock-git",
        "sublime-text-4", "steam", "sudo", "teams", "teamviewer",
        "telegram-desktop", "tor-browser", "tk", "vlc", "wget",
        "wps-office", "woeusb-gui", "yakuake", "yay", "zoom",
        "bpytop", "htop", "ffpmeg"
    ]
    for package in all_packages:
        pacman_install(package_name=package)


def install_media_client_side():
    all_packages = [
        "audacious", "audacity", "obs-studio", "kdenlive",
        "qbittorrent", "ffmpeg"
    ]
    for package in all_packages:
        pacman_install(package_name=package)


def install_media_server_side():
    all_packages = [
        "jellyfin", "radarr", "lidarr", "sonarr",
        "qbittorrent", "ffmpeg"
    ]
    for package in all_packages:
        pacman_install(package_name=package)


def install_developer():
    all_packages = [
        "atom", "eclipse-java", "netbeans", "nano", "vim", "kate",
        "pycharm-community-edition", "python3-pip", "sublime-text-4",
        "tk", "yakuake", "python3", "github-desktop"
    ]
    for package in all_packages:
        pacman_install(package_name=package)


def install_general_purpose():
    all_packages = [
        "audacious", "audacity", "bitwarden", "discord",
        "firefox", "flameshot", "gimp", "kate",
        "kdenlive", "nano", "neofetch",
        "obs-studio", "pamac-aur", "qbittorrent",
        "snapd", "spotify-adblock-git",
        "steam", "sudo", "teams", "teamviewer",
        "telegram-desktop", "tor-browser", "tk", "vlc",
        "wps-office", "woeusb-gui", "yay", "zoom",
        "htop", "ffpmeg"
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
             [1] General Purpose
             [2] Media Interested User
             [3] Media Server
             [4] For Developers
             [5] Upgrade Everything
             [99] Custom for @hirusha-adi  
    """)
    mmo = input("? Please select and option: ")
    if mmo == "1":
        os.system("clear")
        print("""
                                     _                  
      __ _  ___ _ __   ___ _ __ __ _| |  _   _ ___  ___ 
     / _` |/ _ \ '_ \ / _ \ '__/ _` | | | | | / __|/ _ \\
    | (_| |  __/ | | |  __/ | | (_| | | | |_| \__ \  __/
     \__, |\___|_| |_|\___|_|  \__,_|_|  \__,_|___/\___|
     |___/                                              
    
     + You will be installing the packages listed below
        """)
        print("""            audacity, bitwarden, htop, ffpmeg,zoom,
            discord, firefox, flameshot, gimp, kate,
            kdenlive, nano, neofetch, obs-studio, 
            pamac-aur, qbittorrent, snapd, steam,
            spotify-adblock-git,sudo, teams,  vlc,
            teamviewer,telegram-desktop", woeusb-gui,
            tor-browser, tk, wps-office, yay
             """)
        smo1 = input("? Hit enter if you want to continue: ")
        if smo1.lower().startswith("q"):
            exit()
        install_general_purpose()


if __name__ == "__main__":
    ENTIRE_PROGRAM()
