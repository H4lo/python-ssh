#coding: utf-8
import paramiko
import subprocess
import threading
import sys


def ssh_command(ip,username,password,command):
	client = paramiko.SSHClient()
	# 新建一个ssh客户端
	
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	client.connect(ip,username=username,password=password)
	# 连接
	
	ssh_session = client.get_transport().open_session()
	# 连接会话
	
	if ssh_session.active:
		
		ssh_session.exec_command(command)
		print ssh_session.recv(1024)
		# 执行输入的命令并打印出来
		
	return 

	
if __name__ == '__main__':
	try:
		ssh_command(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
	except Exception as e:
		print e
