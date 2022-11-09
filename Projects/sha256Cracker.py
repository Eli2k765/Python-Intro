#Crack sha256 hashes with a wordlist

import hashlib
import sys

def crackHash(hash, wordlist):
    try:
        file = open(wordlist, 'r')
    except:
        print('[-] File not found')
        return
    for word in file.readlines():
        word = word.strip('\n')
        cryptWord = hashlib.sha256(word.encode('utf-8')).hexdigest()
        if cryptWord == hash:
            print('[+] Found Password: ' + word)
            return
    print('[-] Password not in list')
    return

def main():
    if len(sys.argv) == 3:
        hash = sys.argv[1]
        wordlist = sys.argv[2]
        crackHash(hash, wordlist)
    else:
        print('Usage: python3 sha256Cracker.py <hash> <wordlist>')
        print('Example: python3 sha256Cracker.py 5d41402abc4b2a76b9719d911017c592 10-million-password-list-top-1000000.txt')

if __name__ == '__main__':
    main()

