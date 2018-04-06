# Import dependencies
import re
import numpy as np

# Defining the input and output streams
infilename = "Fragaria_x_ananassa-Winter_Dawn_vs_fvesca_v1.1_pseudo.fna.LG1_50K.pileup"
outfilename = "test_out.txt"

# Defining a main function that processes a mpileup file and outputs SNP locations
def call_SNPs(infilename, outfilename):
    
    # Open outfile
    outfile = open(outfilename, "w+")    
    
    # Instantiate temp objects
    temp_pos = gen_pos()
    
    # Iterate through the file checking for variants
    with open(infilename,'r') as infile:
        line_int = 0
        for line in infile:
            line_int += 1
            print(line_int)
            temp_pos = gen_pos()
            temp_pos.readline(line.strip('\n'))
            temp_pos.write_var(outfile)
    
    outfile.close()

# Defining a class that describes a specific position in a genome
class gen_pos:
    # Define full generator that accepts all fields
    def __init__(self, chromosome = "default", coordinate = 0, ref_base = "A", read_ct = 0, reads = "", base_quals = ""):
        self.chromosome = chromosome
        self.coord = coordinate
        self.ref_base = ref_base
        self.read_ct = read_ct
        self.reads = reads
        self.base_quals = base_quals
        self.filter = None
        self.variant_flag = None
        self.variants = np.array([False, False, False, False], dtype = bool)
        self.variant_freq = np.array([0, 0, 0, 0], dtype = float)
    
    # Define a method for extracting a genome position from a .mpileup filestream
        # Origin Date: 
        # Recent Update:
        # Author: Matthew McGowan
        # PRECONDITION: Filestream must be in standard .mpileup format and open for processing
    def readline(self, line):
        #line = infile.readline().rstrip('\n')
        line_split = line.split("\t")
        self.chromosome = line_split[0]
        self.coord = int(line_split[1])
        self.ref_base = line_split[2]
        self.read_ct = int(line_split[3])      
        self.reads = np.asarray(parse_basestring(line_split[4]))
        self.base_quals = convert_qual(line_split[5])
        self.filter = self.check_indel()
        self.variant = self.check_variant()
        
    # A member function that prints a position to an outstream        
    def print(self):
        print(f"Chromosome: {self.chromosome}")
        print(f"Coordinate: {self.coord}")
        print(f"Reference: {self.ref_base}")
        print(f"Read Count: {self.read_ct}")
        print(f"Reads: {self.reads}")
        print(f"Base Qualities: {self.base_quals}")
        print(f"Filter: {self.filter}")
        print(f"Variant Flag: {self.variant_flag}")
        print(f"Variants: {self.variants}")
        print(f"Variant freq: {self.variant_freq}")
        
    # A member function that checks whether an indel is present
    def check_indel(self):
        if (check_indel(self.reads)):
            return True
        else:
            return False
        
    # A member function that checks if a variant is present (returns 1 if true)
    def check_variant(self):
        #print("checking for variant")
        #print(f"Reference: {self.ref_base}")
        #print(f"Reads: {self.reads}")
        #print(f"Quals: {self.base_quals}")
        
        if (not self.filter): # Only check if not filtered
            read_ct = 0
            ref_ct = 0
            a_ct = 0
            t_ct = 0
            c_ct = 0
            g_ct = 0
            
            for i in range(0, len(self.reads)): # Count the reference and variant reads
                char_val = self.reads[i]
                qual_val = self.base_quals[i]
                
                if ((char_val == "." or char_val == ",") and qual_val >=30):
                    read_ct += 1
                    ref_ct += 1
                elif ((char_val == "a" or char_val == "A") and qual_val >=30):
                    read_ct += 1
                    a_ct += 1
                elif ((char_val == "t" or char_val == "T") and qual_val >=30):
                    read_ct += 1
                    t_ct += 1
                elif ((char_val == "c" or char_val == "C") and qual_val >=30):
                    read_ct += 1
                    c_ct += 1
                elif ((char_val == "g" or char_val == "G") and qual_val >=30):
                    read_ct += 1
                    g_ct += 1
            
            #print(f"Reference count: {ref_ct}")
            
            # Check each variant to see if a variant is present
            if (read_ct > 10 and a_ct > 3):
                self.variant_flag = True
                self.variants[0] = True
                self.variant_freq[0] = a_ct / read_ct
                
            if (read_ct > 10 and t_ct > 3):
                self.variant_flag = True
                self.variants[1] = True
                self.variant_freq[1] = t_ct / read_ct
                
            if (read_ct > 10 and c_ct > 3):
                self.variant_flag = True
                self.variants[2] = True
                self.variant_freq[2] = c_ct / read_ct
                
            if (read_ct > 10 and g_ct > 3):
                self.variant_flag = True
                self.variants[3] = True
                self.variant_freq[3] = g_ct / read_ct
    
    # A member function that writes any variants at a position to a file (in tab-delimited format: 'name', 'position', 'reference base', 'variant base', 'variant frequency')
    def write_var(self, outfile):
        if (self.variant_flag):
            if (self.variants[0]): # 'A' variant present
                outfile.write(f"{self.chromosome}\t{self.coord}\t{self.ref_base}\tA\t{round(self.variant_freq[0], 2)}\n")
                
            if (self.variants[1]): # 'A' variant present
                outfile.write(f"{self.chromosome}\t{self.coord}\t{self.ref_base}\tT\t{round(self.variant_freq[1], 2)}\n")
                
            if (self.variants[2]): # 'A' variant present
                outfile.write(f"{self.chromosome}\t{self.coord}\t{self.ref_base}\tC\t{round(self.variant_freq[2], 2)}\n")
                
            if (self.variants[3]): # 'A' variant present
                outfile.write(f"{self.chromosome}\t{self.coord}\t{self.ref_base}\tG\t{round(self.variant_freq[3], 2)}\n")

# Define a function that converts an ASCII quality score string to an integer array
def convert_qual(instring):
    char_array = list(instring)
    int_array = np.empty(len(char_array), dtype=int)
    
    for i in range(0, len(char_array)):
        int_array[i] = ord(char_array[i]) - 33
        
    return int_array

# Define a function that checks a base alignmnet string for indels or reference skips (returns 1 if present)
def check_indel(input):
    flag_chars = ['*', '+', '-', '<', '>']    
    flag = 0
    
    for i in input:
        if (i in flag_chars):
            flag = 1
    return flag

# Define a function that parses a base alignment string, removes unnecessary characters and returns a char array
def parse_basestring(instring):
    temp_string = re.sub(r'\^.', '', instring)
    temp_string = re.sub(r'[$]', '', temp_string)
    return list(temp_string)


# Run the script
call_SNPs(infilename, outfilename)
