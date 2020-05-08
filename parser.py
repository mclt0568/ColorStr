import colors
MARKER_FG = "§"
MARKER_BG = "ƒ"

def parse(text:str):
	broken = []
	breaking = ""
	i = 0
	while i < len(text):
		if text[i] == MARKER_FG:
			broken.append(breaking)
			i += 1
			broken.append(MARKER_FG+text[i])
			breaking = ""
		elif text[i] == MARKER_BG:
			broken.append(breaking)
			i += 1
			broken.append(MARKER_BG+text[i])
			breaking = ""
		else:
			breaking += text[i]
		i += 1
	broken.append(breaking)
	formed = ""
	for i in broken:
		if len(i):
			if i[0] in MARKER_FG:
				if i[1] in colors.FGColors:
					formed+=(colors.FGColors[i[1]])
				elif i[1] in colors.Formats:
					formed+=(colors.Formats[i[1]])
				elif i[1] == MARKER_FG:
					formed+=MARKER_FG
			elif i[0] in MARKER_BG:
				if i[1] in colors.BGColors:
					formed+=(colors.BGColors[i[1]])
				elif i[1] in MARKER_BG:
					formed+=MARKER_BG
			else:
				formed+=(i)
	return formed