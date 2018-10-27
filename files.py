# Open a file
fo = open('test.txt', 'w')

# Get some info
print('File Name: ', fo.name)
print('Is Closed: ', fo.closed)
print('Opening Mode: ', fo.mode)
fo.write('I love Python')
fo.write(" and Javascript")
fo.close()

fo = open('test.txt', 'a')
fo.write('. I also like Django')
fo.close()

fo = open('test.txt', 'r+')
text = fo.read(10)
print(text)
fo.close()

fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close()
