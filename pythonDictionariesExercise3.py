fhand = input('Enter a file name: ')

try:
    file_handle = open(fhand)

except FileNotFoundError:
    print(fhand, 'Could not be found')
    exit()

counts = dict()

for word in file_handle:
    if not word.startswith("From "):
        continue

    words = word.split()
    email = words[1]

    counts[email] = counts.get(email, 0) + 1
print('Counts', counts)
