#Remove vowels

#Write a function that will remove all vowels from a given string. The function should return a string.
#Examples:						
#Input: ‘Joel’
#Output: ‘Jl’
#Input: ‘Shoha’
#Output: ‘Shh’
 
 
 
def removevowels(string):
    vowels = 'aeiou'
    for x in string:
        if x.lower() in vowels:
            string.pop(x)
            print(string)


removevowels('Joel')