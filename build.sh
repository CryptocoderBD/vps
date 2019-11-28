import os
import time
kali = input("YOU WANT TO UPDATE SYSTEM : Y / n ")

if "Y" in kali:
	os.system("locale-gen en_US.UTF-8")
	os.system("apt install dialog -y")
	os.system("apt install nano -y")
	os.system("cd /etc/apt/sources.list.d && rm -rf * && cd .. && rm -rf sources.list")
	time.sleep(5)
	print("KALI LINUX REPO ADDING.......")
	os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
	time.sleep(5)
	print("KALI LINUX PGP ADDING........")
	os.system("wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-key.asc")
	print("KALI LINUX UPDATEING......")
	os.system("sudo apt update --fix-missing")
	print("INSTALLING TOOL ........")
	os.system("apt install wpscan sqlmap python python-pip python3 python3-pip php php-curl curl nodejs -y")
else:
	os.system("exit")
