def main():
	print(check_eq())



def check_eq():
	sim = []
	d_adv = []
	for i in range(1,100):
		d_adv.append(fizzbuzz_adv(i))
		sim.append(fizzbuzz(i))
	
	for i in range(len(sim)):
		try:
			if sim[i] != d_adv[i]:
				print(f"At Number:{i+1}: {sim[i]} != {d_adv[i]}")
				return False
		except IndexError:
			print(f"Not Same Length: sim:{len(sim)} adv:{len(adv)}")
			return False
	return True


def fizzbuzz(count, f=3, b=5, fname="fizz", bname="buzz"):
	res = ""
	if count % f == 0:
		res += fname
	if count % b == 0:
		res += bname
	if res == "":
		return count
	return res

def fizzbuzz_adv(count):
	keyvalues = {"fizz":3,"buzz":5}
	ret = ""
	for k,v in keyvalues.items():
		ret += k if count % v == 0 else ""
	return count if ret == "" else ret


if __name__ == '__main__':
	main()