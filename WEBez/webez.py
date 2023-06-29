#!/usr/share/python3

import subprocess
from art import *
from termcolor import colored

print(colored(text2art("WEBez"), 'cyan'))
print(colored('Created by ByteVigilante\n\n'.center(60), 'red'))

def main():
    choice = input(" 1- Crack MD5 hash (put hash in hash.txt document)\n 2- Exploit\n 3- Search Website Vulnerabilities\n\nPlease Enter a Number: ")
    if choice == '1':
        hash_crack()
    if choice == '2':
        print(subprocess.run(['msfconsole']))
    if choice == '3':
        nikto()

def hash_crack():
    subprocess.run(['hashcat', '-m', '0', '-a', '0', '/usr/share/wordlists/rockyou.txt', '-o', '/home/kali/Desktop/hash.txt'])

def nikto():
    url = input("Enter the Website URL: ")
    subprocess.run(['nikto', '-h', url])

if __name__ == '__main__':
    main()

