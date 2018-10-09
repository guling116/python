#       扫描此局域网的所有IP地址
import platform
import os
import time
import _thread

def get_os():
	os = platform.system()
	if os == 'Windows':
		return 'n'
	else:
		return 'c'
		
def ping_ip(ip_str):
	cmd = ['ping','-{op}'.format(op=get_os()),'1',ip_str]
	
	output = os.popen(' '.join(cmd)).readlines()
	
	for line in list(output):
		if not line:
			continue
		if str(line).upper().find('TTL') >= 0:
			print('%s on' % ip_str)
			break
			
			
def find_ip(ip_prefix):
	for i in range(1,256):
		ip = '%s.%s' % (ip_prefix,i)
		_thread.start_new_thread(ping_ip,(ip,))
		time.sleep(0.3)


if __name__ == '__main__':
	start_time = time.clock()
	ip_prefix = '192.168.3'
	print('%sruning' % ip_prefix)
	find_ip(ip_prefix)
	print('over')

