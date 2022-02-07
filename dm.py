import os, sys
if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("10445439493104456372")
			exit(" [!] Succesfull Deleted")
		else:
			print(" [?] Wellcome : ")
			exit(" [!] Run : python jssl.py remove")
	try:
		__import__("dmx").__main__Main()
	except Exception as e:
		exit(str(e))
 
