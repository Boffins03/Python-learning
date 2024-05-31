import re
x = 'My 2 favorite numbers are 10 and 20'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AIEOU]', x)
print(y)