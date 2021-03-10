##############################

"""
make dictionary for 1-to-3 aa code conversion
"""

# make dictionary that allows lookup of one-letter codes and shows corresponding three-letter codes
code3 = ("Ala", "Arg", "Asn", "Asp", "Cys", "Glu", "Gln", "Gly", "His", 
"Ile", "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", 
"Tyr", "Val")

code1 = ("A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", 
"M", "F", "P", "S", "T", "W", "Y", "V")

aa_dict_1_to_3 = {}

for i in range(len(code1)):
    aa_dict_1_to_3.update({code1[i]: code3[i]})
print(aa_dict_1_to_3)



##############################

"""
program to list out letters from an aa sequence with position numbering
and corresponding aa three-letter codes
"""

# write out a sequence with numbering for each element
def main():
# define aa one-letter & three-letter conversion dictionaries
    aa_dict_3_to_1 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    
    aa_dict_1_to_3 = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
                      'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
                      'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
                      'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
                      'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}
    
    def spell_string(seq):
        letters = list(seq)
        i = 1
        for element in letters:
            # highlight non-caps letter
            # convert the lookup letter to caps, since that's what's in our conversion dictionaries
            if element != element.upper():
                print(str(i) + " " + element + " " + aa_dict_1_to_3[element.upper()] + " ***") 
            else:
               print(str(i) + " " + element + " " + aa_dict_1_to_3[element.upper()]) 
            i +=1
    
    seq_name = input("Sequence name =\n") 
    seq = input("Sequence (using one-letter codes) =\n")
    
    print("\nSequence name = " + seq_name)
    
    spell_string(seq)

main()



##############################

"""
change aa at a given position in your sequence
"""
def main():
    aa_dict_3_to_1 = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    
    aa_dict_1_to_3 = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
                      'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
                      'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
                      'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
                      'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}
    
    def spell_list(letters):
        i = 1
        for element in letters:
            # convert the lookup letter to caps, since that's what's in our conversion dictionaries
            print(str(i) + " " + element + " " + aa_dict_1_to_3[element.upper()]) 
            i +=1

    seq_name = input("Sequence name =\n") 
    seq = input("Sequence (using one-letter codes) =\n")
    
    #print("\nSequence name = " + seq_name)
    letters = list(seq)
    
    position = int(input("Position number to change = "))
    
    old_aa = letters[position-1]
    print("Current aa = " + old_aa +"\n")
    
    new_aa = input("Replacement aa (one-letter code) = ")
    print("\nNew sequence is:")
    
    
    letters[position-1] = new_aa

    spell_list(letters)
    
main()



##############################


