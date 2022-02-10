import csv

words = [] #List to hold file contents

file = open("/home/ilias/Documents/Big Data/__pycache__/sample-2mb-text-file.txt", "r") #Opening file

words = file.read().split() #Reading the file and splitting it into words

#Creating a new file as csv and writing the results
with open("/home/ilias/Documents/Big Data/__pycache__/words.csv", "w", newline='') as wfl:
    csvwriter = csv.writer(wfl, delimiter=',')
    for row in words:
        csvwriter.writerow([row])