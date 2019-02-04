# 
#                  bible-parser2000
#  * Removes empty lines and titles from a bible.
#  * Arranges the remaining lines so that each line
#       starts with a chapter and a verse.
#  * Adds a delim after the first two words.
# 
#  Please use python3 instead of python2.7.
#
#
# Empty lines are boring
# -> no empty lines
# Old testament titles are fully capitalized
# -> no fully capitalized lines
# New testament titles start with a tab
# -> no lines starting with a tab
#

filename = input("Enter your bible filename: ")
delim =  input("Enter the delim for SQL exporting, space for no delim: ")

with open(filename, "r") as bible, open("parsedbible.txt","w") as parsedbible:

    previousline = ""

    for line in bible:
        
        # ignore empty, tabulated and fully capitalized lines
        if line == "\n" or line.startswith("\t") or line.isupper():
            continue
        
        line = line.lstrip() # remove white space from right side
        line = line.replace("\n", "") # remove all endlines
        
        words = line.split()
        
        # If the current line is too short or
        # the 2nd word is nort a verse (e.g. 12:34),
        # append the current line to the previous line.
        if len(words) < 3:
            previousline = previousline + " " + line
        elif ":" not in words[1] or words[1].replace(":", "").isalpha():
            previousline = previousline + " " + line
        
        else:
            
            # make chapter name lowercase, e.g. 1Moos. -> 1moos.
            line = line.replace(words[0], words[0].lower(), 1)
            
            if "." in words[0]:
                # remove a period from chapter, e.g. 1moos. -> 1moos
                line = line.replace(".", "", 1)
            if "." in words[1]:
                # remove a period from verse, e.g. 12:34. -> 12:34
                line = line.replace(".", "", 1)
            
            line = line.replace(" ", delim, 2) # change two first spaces into %
            if previousline != "":
                parsedbible.write(previousline + "\n")
            previousline = line
    
    # collect the last remaining line
    parsedbible.write(previousline)
            
        
