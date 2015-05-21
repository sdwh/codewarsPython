def splitInteger(num,parts):
    mul,mod = divmod(num,parts)
    return [mul] * parts

print(splitInteger(23,2))


#We need the ability to divide an unknown integer 
#into a given number of even parts — or at least as even as they can be. 
#The sum of the parts should be the original value,
# but each part should be an integer, 
#and they should be as close as possible.