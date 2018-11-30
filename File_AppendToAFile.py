import datetime

# w: indicates append
# +: means it will create a file if it does not exist in library
# 'a+'
file = open("test2.txt","a")
t = datetime.datetime.now()

for i in range(1, 10):
	file.write('{}: line {}\n'.format(t, i))

file.write('\n')	# create a empty line after writing finishes

file.close()
