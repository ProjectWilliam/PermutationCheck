#!/usr/bin/python
# Author: William Guerrero

# Given two strings determine if one is a permutation of the other

str1 = raw_input('Please input the first string: ')

str3 = list(str1)

str2 = raw_input('Please input the second string: ')

str4 = list(str2)


def PermutationCheck(string1, string2): 

	counter = 0

	if (len(string1) == len(string2)): #Condition 1: Permutations have the same length
  
  		for i in range(len(string1)):
 	
 			for j in range(len(string2)):
 		
 				if (string1[i] is string2[j]): 
 
 					counter += 1
 				
 					#Filler for array position to enable checking more than one of same letter
 				
 					string1[i] = '2'
 				
 					string2[j] = '2'
 	
	
		if (counter == len(string1)):
 	
			print 'Strings are permutations of one another'
 				
 
 	else: 
 
 		print 'Neither of the strings are a permutation of the other'
 
 		return False; 
 
 
 #call function
 
PermutationCheck(str3, str4);