import colorstrparser,sys

def parse(value):
	return colorstrparser.parse(value)

if __name__ == "__main__":
	if sys.argv[1:]:
		print(colorstrparser.parse(sys.argv[1]))
	else:
		print("Please provide string as argument.")
