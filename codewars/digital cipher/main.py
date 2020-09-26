import time

def encode(message, key):
	ret = []
	d = dict()
	[d.update({chr(i):i-96}) for i in range(97,123)]
	for i in range(len(message)):
		ret.append(d[message[i]]+int(str(key)[i%len(str(key))]))
	return ret




def solve(n):
	ret = ""
	seq = ""
	for i in range(1,n+1):
		seq += str(i)
		ret += seq
		if len(ret) > n:
			break
	return "".join(ret)[n-1]


start_time = time.time()
print(solve(2100))
print("--- %s seconds ---" % (time.time() - start_time))

def solve(n):
	ret = "1"
	if n == 1:
		return ret[0]
	for i in range(1,n+1):
	    ret += (ret[i-1]+str(i+1))
	return "".join(ret)[n-1]

start_time = time.time()
print(solve(2100))
print("--- %s seconds ---" % (time.time() - start_time))
