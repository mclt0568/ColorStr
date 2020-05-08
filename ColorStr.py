import parser,sys

def parse(value):
	return parse.parse(value)

if __name__ == "__main__":
	if sys.argv[1:]:
		print(parser.parse(sys.argv[1]))
	else:
		print("Please provide string as argument.")