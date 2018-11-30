my_list = [True, True, False, True, False]


if any(my_list):
	print('At least one of them is TRUE')


if all(my_list):
	print('All of them is TRUE')


import wikipedia
result = wikipedia.page('python3')
print(result.summary)
for link in result.links:
	print(link)