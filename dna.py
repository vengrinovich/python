"""Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!

The project should have methods for each of the following:

Given a file, read in the DNA for each suspect and save it as a string
Take a DNA string and split it into a list of codons
Iterate through a suspect's codon list to see how many of their codons match the sample codons
Pick the right suspect to continue the investigation on"""

sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
	dna_data = ''
	with open(dna_file,'r') as f:
		for line in f:
			dna_data += line
	return dna_data

def dna_codons(dna):
	codons = []
	for x in range(0, len(dna), 3):
		if (x + 3) <= len(dna):
			codons.append(dna[x:x + 3])
	return codons

def match_dna(dna):
	matches = 0
	for i in dna:
		if i in sample:
			matches += 1
	return matches

def is_criminal(dna_sample):
	dna_data = read_dna(dna_sample)
	codons = dna_codons(dna_data)
	num_matches = match_dna(codons)
	if num_matches >= 3:
		print "Investigation should continue"
	else:
		print "Number of matches is %d, the suspect can be freed" % num_matches 


is_criminal('suspect1.txt')
is_criminal('suspect2.txt')
is_criminal('suspect3.txt')

