'''
ASTHA PRIYA 
CS - A
20219024
LZW Compression
'''

def encode(string):
	table = dict()
	lis = []
	for i in range(256):
		table[chr(i)] = i
	current = ''
	nxt_code = 257
	for i in string:
		current+=i
		if(current not in table):
			table[current] = nxt_code
			nxt_code += 1
			current = current[:-1]
			lis.append(table[current])
			current = i
		lis.append(table[current])
		return lis

def decode(lis):
	table = dict()
	for i in range(256):
		table[i] = chr(i)
	prev = ''
	nxt_code = 257
	ans = ''
	for i in lis:
		ans+=table[i]
		if(prev != ''):
			table[nxt_code] = prev+table[i][0]
			nxt_code+=1
		prev = table[i]
	return ans

def main():
	lis = []
	msg = input("ENTER THE MESSAGE: ")
	lis = encode(msg)
	print("AFTER COMPRESSION: ",lis)
	ans = decode(lis)
	print("AFTER DECOMPRESSION: ",ans)

if __name__ == '__main__':
	main()

'''
OUTPUT:
ENTER THE MESSAGE: Hello
AFTER COMPRESSION:  [72,101,108,108,111]
AFTER DECOMPRESSION:  Hello
'''
