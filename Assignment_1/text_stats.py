# read data the intput file (named input,txt)

def read_file(file_path):
    '''Reads the content of a file and returns it as a string.'''
    with open(file_path, 'r') as file:
        return file.read()

# read it into a variable
text = read_file('input_1.txt')

# process (parse) (clean it!) (get it ready for...???) -analysis

# remove the punctuation and extra whitspace \n \t \s

# normalization (lowercase the text)

# make it so we can compare our data

# tokenization (split the string into it's component parts)

# .split() \ - (returns a list of strings)


# calculate/accumulate statistics
# setup varaibles/data structures for our data
# Len() - will give us the word count and char
# set() - will give unique word count 
# avarage word count 


# output the stats to the terminal and a file (output.txt)
# (in the presribed format)


def character_count_with_spaces(text): 
    return len(text)

def character_count_no_spaces(text):
    return len(text.replace(" ", "").replace("\n", "").replace("\t", ""))



print(character_count_no_spaces(text))
