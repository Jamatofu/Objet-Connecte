import sys
import os


def executeNodeRed(name):
	print(name)
	if(name == "server"):
		os.system('node-red --userDir NR_orchestreur/ flow.json')
	else:
		os.system('node-red --userDir NR_raspberry/ flow.json')

if __name__ == "__main__":
    if len(sys.argv) == 2 :
    	executeNodeRed(sys.argv[1])


	