from multiprocessing import *
import csv

def half1():
    #List to hold the file's contets
    words = []

    #Opening the csv file
    with open("words.csv", "r") as fl:
        csvreader = csv.reader(fl)
        #Appending the csv's contents to a list
        for row in csvreader:
            words.append(row)

    #Counting how many times a word appears and writing it back to the list
    for i in range(int(len(words)/2)): #For each word
        count = 0 #Counter to keep track of times of appearance
        for j in range(i+1, int(len(words)/2)): #For each word after the one we "selected" above
            if(words[i] == words[j]): #If the words are the same
                count += 1    #Count
            words[i] = (words[i], ',', count) #Write the result back to our first word

    return(words) #Return the new list

def half2():
    #List to hold the file's contets
    words = []
    
    #Opening the csv file
    with open("words.csv") as fl:
        csvreader = csv.reader(fl)
        #Appending the csv's contents to a list
        for row in csvreader:
            words.append(row)
    
    #Counting how many times a word appears and writing it back to the list
    for i in range(int((len(words)/2)+1),len(words)): #For each word
        count = 0 #Counter to keep track of times of appearance
        for j in range(i+1, len(words)): #For each word after the one we "selected" above
            if(words[i] == words[j]): #If the words are the same
                count += 1 #Count
            words[i] = (words[i], ',', count) #Write the result back to our first word

    return(words) #Return the new list

if(__name__ == "__main__"):
    #Lists to hold the data the functions return
    words1 = []
    words2 = []

    #Initializing the processes
    p1 = Process(target = half1)
    p2 = Process(target = half2)

    #Starting the processes and saving their results
    words1 = p1.start()
    words2 = p2.start()

    #"Stopping" the processes
    p1.join()
    p2.join()
