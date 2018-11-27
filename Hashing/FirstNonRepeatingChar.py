'''
Given a stream of characters, find the first non-repeating character from stream. 
You need to tell the first non-repeating character in O(1) time at any moment.

Follow up : Use constant auxiliary space; the stream can be considered as a list; no need to consider file;

Interview tags: Microsoft Amazon Flipkart Payu Yahoo

Author : @amitrajitbose
'''

def first_non_repeating(stream):
  charhash={}
  for i in range(256):
    charhash[i]=0

  charqueue=[]
  stream=list(stream)
  for ch in stream:
    print("Reading",ch,"from stream")
    i=ord(ch)
    if(charhash[i]==0):
      #first occurance
      charhash[i]+=1
      charqueue.append(ch)
    elif(charhash[i]==1):
      #second occurance
      charqueue.remove(ch)
      charhash[i]+=1
    #we don;t need to care about further occurance
    if(len(charqueue)>0):
      print("First non-repeating character so far is ",charqueue[0])
    else:
      print("First non-repeating character so far is nothing")

stream = "geeksforgeeksandgeeksquizfor"
first_non_repeating(stream)
