import sys
import os


def executeNodeRed(name):
	if name == "server":
		os.system('node-red --userDir NR_orchestreur/ flows_L50-FK.json')
	if name == "rasp":
		os.system('node-red --userDir NR_raspberry/ flows_raspberrypi.json')
	if name == "ihm":
		os.system('node-red --userDir NR_IHM/ flow.json')

if __name__ == "__main__":
    if len(sys.argv) == 2 :
    	executeNodeRed(sys.argv[1])


	
