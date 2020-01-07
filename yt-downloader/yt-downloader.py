import subprocess,os
    
def download(datalinks):
    print("downloading: "+str(datalinks))
    command="youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "+str(datalinks)
    process = subprocess.Popen(command, shell=True)
    process.wait()
    print(process.returncode)
    print("download complete..")


def initscraper():
    # Taking Input from user
    keyword = input("Enter your youtube playlist : ") 
    download(keyword)
    # ===============================================
def banner():
    os.system('clear')

    print("##    ## ########         ########   #######  ##      ## ##    ## ##        #######     ###    ########  ######## ########  ")
    print(" ##  ##     ##            ##     ## ##     ## ##  ##  ## ###   ## ##       ##     ##   ## ##   ##     ## ##       ##     ## ")
    print("  ####      ##            ##     ## ##     ## ##  ##  ## ####  ## ##       ##     ##  ##   ##  ##     ## ##       ##     ## ")
    print("   ##       ##    ####### ##     ## ##     ## ##  ##  ## ## ## ## ##       ##     ## ##     ## ##     ## ######   ########  ")
    print("   ##       ##            ##     ## ##     ## ##  ##  ## ##  #### ##       ##     ## ######### ##     ## ##       ##   ##   ")
    print("   ##       ##            ##     ## ##     ## ##  ##  ## ##   ### ##       ##     ## ##     ## ##     ## ##       ##    ##  ")
    print("   ##       ##            ########   #######   ###  ###  ##    ## ########  #######  ##     ## ########  ######## ##     ## ")
    print("======================================================Created By D-eviloper=================================================")
    print("===================================================Downloads Youtube Playlist===============================================")
    print("\n")
    initscraper()

banner()

