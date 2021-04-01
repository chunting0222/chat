
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # -sig為另一個版本，去除開頭編碼\ufeff的方法
		for line in f:
			lines.append(line.strip())
	return lines


def convert(Lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	for line in Lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				allen_word_count += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				viki_word_count += len(m)
	print('Allen說了', allen_word_count)
	print('Viki說了', viki_word_count)




def write_file(filename, Lines):
	with open(filename, 'w') as f:
		for line in Lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)

main()