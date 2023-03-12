import subprocess #excute system command
from discordwebhook import Discord
import time

discord = Discord(url="https://discord.com/api/webhooks/1084390591154102373/zSKtCxgU_pDo81YDsu2q3VqNp3bw343-e52giiRbwYiXeJ-GC8Eus23wSAsWZqTYb4KF")

def send(msg):
    discord.post(content=msg)
    return True

def automation(domain):
    subprocess.call(f"subfinder -d {domain} -o subfinder_automate.txt", shell=True)
    new_subdomains = subprocess.check_output("cat_subfinder_automate.txt",shell=True).decode('utf-8').split()
    old_subdomains = subprocess.check_output("cat old_subdomains.txt",shell=True).decode('utf-8').split()
    if len(new_subdomains) != len(old_subdomains):
        send("Hey Jay! We've found something new ")
        for subdomain in new_subdomains:
            if subdomain not in old_subdomains:
                send(f"Found a new subdomain: {subdomain}")

domain_name = input("Enter the domain name: ")

while True:
    automation(domain_name)
    time.sleep(604800)


