def overworldToNeather(x,y,z):
	return f"x:{x/8} y:{y} z:{z/8}"
def neatherToOverworld(x,y,z):
	return f"x:{x*8} y:{y} z:{z*8}"

import sys
def main():
	argc = len(sys.argv)
	argv = sys.argv
	if argc > 1+3:
		if '-n' in argv[1]:
			print(neatherToOverworld(int(argv[2]),int(argv[3]),int(argv[4])))
		if '-o' in argv[1]:
			print(overworldToNeather(int(argv[2]),int(argv[3]),int(argv[4])))


if __name__ == '__main__':
	main()