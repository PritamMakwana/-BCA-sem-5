# reading source code of a website page from Internet
import urllib.request
# store the url of the page into the file object
file = urllib.request.urlopen("https://kscpac.org/")
# read data from file and display
print(file.read())