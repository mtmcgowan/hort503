"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.
      
.. moduleauthor:: Matthew McGowan

"""

import sys

class read:
    # Initialize the read to be all empty strings
    def __init__(self):
        self.seq_id = ""
        self.seq = ""
        self.seq_id2 = "",
        self.quality_str = ""

    # get_read method: gets values for each field by successively reading in lines from the filestream
    # Prereq: infile should be properly formatted and pointing to the start of the file
    def get_read(self, infile):
        self.seq_id = infile.readline()
        self.seq = list(infile.readline()) # Coerce the sequence string into a list array
        self.seq_id2 = infile.readline()
        self.quality_str = list(infile.readline()) # Coerce the quality string into a list array

    # write method: Writes a fastq read to a file
    # Prereq: outfile must be open and available for writing
    def write(self, outfile):
        outfile.write(self.seq_id)
        outfile.write("".join(self.seq))
        outfile.write(self.seq_id2)
        outfile.write("".join(self.quality_str))

    # trim_read_front method: trims the front of a sequence using a minimum quality threshold
    def trim_read_front(self, min_qual):
        #print("Quality string:", self.quality_str)
        index = 0 
        flag = 0       
        while((index < len(self.quality_str)) & (flag != 1)): # Check whether the current index score is below the threshold
            if (str_to_score(self.quality_str[index]) < min_qual):
                #print("Read value:", ord(self.quality_str[index])-33) 
                del(self.quality_str[index]) # remove the quality score
                del(self.seq[index]) # remove the sequence value
                #print("Quality string:", self.quality_str)
            else:
                flag = 1
            
            #index += 1   

# str_to_score function: Converts an ascii character to a quality score
def str_to_score(character):
    return (ord(character) - 33)

# min_seq_start function: Determines the minimum quality score present at the first position of a sequence in a fastq file
def min_seq_start(filename):
    file = open(filename, "r")

    # Determine the number of lines/sequences in a file
    num_lines = sum(1 for line in open(filename))
    rem_reads = num_lines%4
    num_reads = num_lines//4

    min_score = 100

    if (rem_reads == 0):   # Only continue if the linecount is a factor of 4 (rough indicator for correct formatting)     
        for i in range(num_reads):
            curr_read = read()
            curr_read.get_read(file)
            #print(str_to_score(curr_read.quality_str[0]))
            start_score = str_to_score(curr_read.quality_str[0])
            if start_score < min_score:
                min_score = start_score   
            
    else:
        print("File incorrectly formatted!") 

    file.close()
    return min_score

# The main function for the script.
def main(argv):   
    # import in arguments
    infile_name = argv[1]
    outfile_name = argv[2]
    min_qual = int(argv[3])
    min_len = int(argv[4])

    min_score =  min_seq_start(infile_name)
    print("Original file minimum start score:", min_score)

    # open files for reading/writing
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")
    
    # Determine the number of lines/sequences in a file
    num_lines = sum(1 for line in open(infile_name))
    rem_reads = num_lines%4
    num_reads = num_lines//4

    if (rem_reads == 0):   # Only continue if the linecount is a factor of 4 (rough indicator for correct formatting)     
        for i in range(num_reads):
            curr_read = read()
            curr_read.get_read(infile)
            curr_read.trim_read_front(min_qual)
            if (len(curr_read.seq) >= min_len+1):
                curr_read.write(outfile)
    else:
        print("File incorrectly formatted!")         

    infile.close()
    outfile.close()

    print("Trimmed file minimum start score:", min_seq_start(outfile_name))
    

# Begin the program by calling the main function.
main(sys.argv)

