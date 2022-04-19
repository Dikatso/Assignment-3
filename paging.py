#Dikatso Moshweunyane
#CSC3002F ASSIGNMENT 3
#18 APRIL 2022

import sys
from random import randint

def FIFO(size, pages):
    frames = []                 #List to store frames in memory
    page_len = len(pages)
    iterator = 0
    numFaults = 0

    while (iterator < page_len):
        if (pages[iterator] not in frames):     # Checks if page is not in frame
            numFaults = numFaults + 1           # Page fault occured 
            if (len(frames) >= size):           # Checks if frame is full, if true the first page is deleted
                frames.pop(0)
            frames.append(pages[iterator])      #New frame added
        iterator = iterator + 1

    return numFaults

def LRU(size,pages):
    frames = []                 #List to store frames in memory
    page_len = len(pages)
    iterator = 0
    numFaults = 0

    while (iterator < page_len):
        if (pages[iterator] not in frames):      # Checks if page is not in frame
            numFaults = numFaults + 1            # Page fault occured
            if (len(frames) >= size):
                frames.remove(frames[0])         #Remove first occurrence of value
                frames.append(pages[iterator])
            else:
                frames.append(pages[iterator])
        else:   #If page exists in frame, remove it and append it
            frames.remove(pages[iterator])
            frames.append(pages[iterator])
        iterator = iterator + 1
        
    return numFaults


def OPT(size,pages):
    pages_copy = pages.copy()       # Create a copy of the pages list
    frames = []                     # List to stroe frames
    page_len = len(pages)
    iterator = 0
    numFaults = 0

    while (iterator < page_len):
        pages_copy.pop(0)           # Remove first value of the copy pages list
        if (pages[iterator] not in frames):        # Checks if page is not in frame
            numFaults = numFaults + 1              # Page fault occured
            if len(frames) < size:                 # Checks if frames list is not full
                frames.append(pages[iterator])

            else:                    
                if len(pages_copy) > 0: 
                    # Fetches the index of the frame to be removed and removes it while inserting new page into frame    
                    deleteFrame = removeFrame(frames, pages_copy)   
                    if deleteFrame != -1:
                        frames.remove(frames[deleteFrame])
                        frames.insert(deleteFrame, pages[iterator])

                    else:
                        frames.pop(0)

                else:
                    break
        iterator = iterator + 1
    return numFaults

def removeFrame(frames,pages_copy):
    page_index_dict = []    # Stores the pages with their respective index
    outputList =[]          # Stores the indexes of the elements in the frames
    optIndex = 0

    for i in range(len(pages_copy)):        # Populates page_index_dict with pages and their indexes
        currentIndex = [pages_copy[i],i]
        page_index_dict.append(currentIndex)

    max_add = 100
    for frame in frames:        #Iterates through frames list
        i = 0                   #While loop iterator
        checkInt = 0            #Tracks how far are we into the page_index_dict list 
        while i < len(page_index_dict):
            if frame == page_index_dict[i][0]:      #checks if frame in page_index_dict, if yes append it's indec to outputList
                outputList.append(page_index_dict[i][1])
                break
            else:
                checkInt += 1

            if checkInt == len(page_index_dict):
                outputList.append(max_add)
                max_add +=1

            i += 1

    optIndex = outputList.index(max(outputList))
    return optIndex

def main():
    # Generating Page Reference Array
    size = int(sys.argv[1])
    size = 3
    pages = []
    page_size = int(input("Enter the length of the page reference array: "))
    for i in range(page_size):
        pages.append(randint(0, 9)) 

    print ("FIFO", FIFO(size, pages), "page faults.")
    print ("LRU", LRU(size, pages), "page faults.")
    print ("OPT", OPT(size, pages), "page faults.")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ("Usage: python paging.py [number of pages]")
    else:
        main()