import os
import time
print('''


$$\   $$\  $$$$$$\  $$\       $$$$$$\       $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
$$ | $$  |$$  __$$\ $$ |      \_$$  _|      \__$$  __|$$  __$$\ $$  __$$\ $$ |      
$$ |$$  / $$ /  $$ |$$ |        $$ |           $$ |   $$ /  $$ |$$ /  $$ |$$ |      
$$$$$  /  $$$$$$$$ |$$ |        $$ |           $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$  $$<   $$  __$$ |$$ |        $$ |           $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |\$$\  $$ |  $$ |$$ |        $$ |           $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ | \$$\ $$ |  $$ |$$$$$$$$\ $$$$$$\          $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
\__|  \__|\__|  \__|\________|\______|         \__|    \______/  \______/ \________|
                                                                                    
            CODED BY ALI KHAN BANGLADESHI HACKER (CryptocoderBD) 
	      FOR FREE WORDPRESS TOOL PLEASE CONTACT WITH ME
                                                                                    
''')

input("PRESS ENTER TO INSTALL KALI LINUX.......")
os.system("locale-gen en_US.UTF-8")
os.system("apt install dialog -y")
os.system("apt install nano -y")
os.system("cd /etc/apt/sources.list.d && rm -rf * && cd .. && rm -rf sources.list")
time.sleep(5)
print("KALI LINUX REPO ADDING.......")
os.system("echo '# Kali linux repositories | Added by Ali Khan\ndeb http://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list")
os.system("echo '# Kali linux repositories | Added by Ali Khan\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list")
time.sleep(5)
print("KALI LINUX PGP ADDING........")
os.system("wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-key.asc")
print("KALI LINUX UPDATEING......")
os.system("sudo apt update --fix-missing")
print("INSTALLING TOOL ........")
os.system("apt install wpscan sqlmap python python-pip python3 python3-pip php php-curl curl nodejs goleng nmap nikto sublist3r figlet -y")
print("Cloning Some Tools.............")
time.sleep(2)
os.system('git clone https://github.com/projectdiscovery/nuclei.git')
os.system('git clone https://github.com/projectdiscovery/nuclei-templates.git')
os.system('git clone https://github.com/projectdiscovery/httpx.git')
os.system('git clone https://github.com/projectdiscovery/shuffledns.git')
os.system('git clone https://github.com/projectdiscovery/dnsprobe.git')
os.system('git clone https://github.com/s0md3v/XSStrike.git')
os.system('git clone https://github.com/bambish/ScanQLi.git')
os.system('git clone https://github.com/m4ll0k/WAScan.git')
os.system('git clone https://github.com/ffuf/ffuf.git')
os.system('git clone https://github.com/MisterSpyx/Mister-Spy-V7.git')
os.system('git clone https://github.com/s0md3v/Corsy.git')
print("All TOOLS INSTALLED >>>>>>>>>.. ")
time.sleep(2)
os.system("figlet KALI_LINUX_INSTALLED.......")
