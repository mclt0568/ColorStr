escapeSeq = "\033[{}m".format


FGColors = {
	"k":escapeSeq("30"),
	"r":escapeSeq("31"),
	"g":escapeSeq("32"),
	"y":escapeSeq("33"),
	"b":escapeSeq("34"),
	"m":escapeSeq("35"),
	"c":escapeSeq("36"),
	"w":escapeSeq("37"),
	"K":escapeSeq("30;1"),
	"R":escapeSeq("31;1"),
	"G":escapeSeq("32;1"),
	"Y":escapeSeq("33;1"),
	"B":escapeSeq("34;1"),
	"M":escapeSeq("35;1"),
	"C":escapeSeq("36;1"),
	"W":escapeSeq("37;1")}

BGColors={
	"k":escapeSeq("40"),
	"r":escapeSeq("41"),
	"g":escapeSeq("42"),
	"y":escapeSeq("44"),
	"b":escapeSeq("44"),
	"m":escapeSeq("45"),
	"c":escapeSeq("46"),
	"w":escapeSeq("47"),
	"K":escapeSeq("40;1"),
	"R":escapeSeq("41;1"),
	"G":escapeSeq("42;1"),
	"Y":escapeSeq("44;1"),
	"B":escapeSeq("44;1"),
	"M":escapeSeq("45;1"),
	"C":escapeSeq("46;1"),
	"W":escapeSeq("47;1")}

Formats={
	"0":escapeSeq("0"),
	"1":escapeSeq("1"),
	"2":escapeSeq("2"),
	"3":escapeSeq("3"),
	"4":escapeSeq("4"),
	"5":escapeSeq("5"),
	"6":escapeSeq("6"),
	"7":escapeSeq("7"),
	"8":escapeSeq("8"),
	"9":escapeSeq("9")}
