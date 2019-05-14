#This program is to check homograph attack.
#!/usr/bin/python -tt
import re
def main():
	try:
		url=raw_input("Enter the value: ")
		check_evil=""
		for i in url:
			check_evil+=i.encode("unicode_escape")
		print "Check Evil", check_evil
		#pattern=re.compile(r'^\w+./')
		pattern=re.compile(r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/#[\]@!\$&\(\)\*\+,;=.]+$')
		print "pattern check", pattern.findall(check_evil)
		if pattern.findall(check_evil):
			print "URL entered is Correct"
		else:
			print "URL entered is not correct"
	except:
		print "Exception"
if __name__ == "__main__":
	main()