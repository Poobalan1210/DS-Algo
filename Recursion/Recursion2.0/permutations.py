def permutations(str):
  if len(str)==0:  #base case when string is empty
    return ['']

  if len(str)==1: #base case when string has length 1
    return [str]
  
  #base case when string has more length
  permlist=[]
  for i in range(len(str)):
    
    perms=permutations(str[:i]+str[i+1:])
    for element in perms:
      permlist.append(str[i]+element)

  return permlist

def main():
    print(permutations('a'))
    print(permutations('abc'))
    print(permutations('ab'))
    print(permutations(''))
    
if __name__=="__main__":
    main()