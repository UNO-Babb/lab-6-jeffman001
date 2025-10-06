#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  linecount = 0
  wordcount = 0
  lettercount = 0
  for line in textFile:
    linecount = linecount + 1
    print(line)
    words = line.split()
    for w in words:
      wordcount = wordcount + 1
      for ch in w: 
        lettercount = lettercount + 1

  
  
#printing results
  print("lines:", linecount)
  print("words:", wordcount)
  print("characters:", lettercount)
if __name__ == '__main__':
  main()
