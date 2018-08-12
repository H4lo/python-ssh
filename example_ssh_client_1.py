#coding: utf-8
import paramiko
import subprocess
import threading
import sys


def ssh_command(ip,username,password):
	client = paramiko.SSHClient()
	# 新建一个ssh客户端
	
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	client.connect(ip,username=username,password=password)
	# 连接
	
	ssh_session = client.get_transport().open_session()
	# 连接会话
	
	if ssh_session.active:
		flag = 1
		
		print 'Enter a command: (exit with \'q\')'
		while(flag):
			ssh_session = client.get_transport().open_session()
			# 这里必须每次都确认一次会话
			
			command = raw_input('>>')
			if command == 'q':
				flag = 0
			ssh_session.exec_command(command)
			print ssh_session.recv(1024)
			# 执行输入的命令并打印出来
	client.close()
	return 

	
if __name__ == '__main__':
	try:
		ssh_command(sys.argv[1],sys.argv[2],sys.argv[3])
	except Exception as e:
		print e
