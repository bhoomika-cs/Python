#Way to create file and handling it
file = open('youtube.txt', 'w')

try:
    file.write('Hello')
finally:
    file.close()

#Another way 
with open('youtube2.txt', 'w') as file:
    file.write('Helloo Bhoomii')