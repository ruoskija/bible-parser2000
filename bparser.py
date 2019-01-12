# 
#              bible-parser2000
# removes boring lines and titles from a bible
# 
# Empty lines are boring
# -> no empty lines
# Old testament titles are fully capitalized
# -> no fully capitalized lines
# New testament titles start with a tab
# -> no lines starting with a tab
#

filename = input("Enter your bible filename: ")
with open(filename, "r") as bible, open("parsedbible.txt","w") as parsedbible:

    for line in bible:
    
        if line == "\n" or line.startswith("\t") or line.isupper():
            continue
        parsedbible.write(line)
        
