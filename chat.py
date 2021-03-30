
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # -sig為另一個版本，去除開頭編碼\ufeff的方法
		for line in f:
			lines.append(line.strip())
	return lines

def convert(Lines):
	new = []
	person = None
	for line in Lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, Lines):
	with open(filename, 'w') as f:
		for line in Lines:
			f.write(line + '\n')

def main()
	lines = read_files('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()