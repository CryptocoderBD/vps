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

kali = input("YOU WANT TO UPDATE SYSTEM : YES / NO ")

if "Y" or "YES" or "yes" or "y" or "Yes" or "YEs" in kali:
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
	os.system("apt install wpscan sqlmap python python-pip python3 python3-pip php php-curl curl nodejs terminator firefox figlet -y")
	
else:
	os.system("exit")
