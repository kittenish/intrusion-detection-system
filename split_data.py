import numpy as np
package = {}
flag = {'OTH': 10, 'RSTR': 3, 'S3': 8, 'S2': 9, 'S1': 6, 'S0': 1, 'RSTOS0': 7, 'REJ': 2, 'SH': 4, 'RSTO': 5, 'SF': 0}

def split_data(url, tcp_finger, label_2):

	f = open(url)
	line = f.readline()
	i = 0
	while line:
		line = line.split(',')
		temp = str(line[1]) + '_' + str(line[2]) 
		if not package.has_key(temp):
			package[temp] = 1
		if temp == 'icmp_eco_i':
			line[3] = flag[line[3]]
			tcp_finger[i,0] = line[0]
			tcp_finger[i,1:] = line[3:41]
			if line[41] == 'normal':
				label_2[0, i] = 0
			else:
				label_2[0, i] = 1
			i = i + 1
		line = f.readline()
	print sorted(package)
	return tcp_finger, label_2

if __name__ == '__main__':
	
	tcp_finger_train = np.zeros([4586, 39])
	label_2_train = np.zeros([1, 4586])
	url = './NSL_KDD/KDDTrain+.txt'
	tcp_finger_train, label_2_train = split_data(url, tcp_finger_train, label_2_train)
	tcp_finger_test = np.zeros([262, 39])
	label_2_test = np.zeros([1, 262])
	url = './NSL_KDD/KDDTest+.txt'
	tcp_finger_test, label_2_test = split_data(url, tcp_finger_test, label_2_test)
	
	#np.savez('./feature/icmp_eco_i.npz', x_train=tcp_finger_train, x_test=tcp_finger_test, y_train=label_2_train, y_test=label_2_test)