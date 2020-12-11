title = "G r een L a ntern C o rp"

counter = 0

while counter < len(title):
    if(counter %2) == 0 and title[counter] != '':
        print(title[counter])
    counter += 1