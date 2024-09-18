if __name__ == "__main__":
  myfile = open("example.txt")
  x = myfile
  myfile2 = open("example2.txt","w")
  myfile2.write("This file contains \n example text \n to be copied")
  myfile.close()
  myfile2.close()