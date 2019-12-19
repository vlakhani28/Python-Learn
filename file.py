fp = open("vaibhav.txt","x")
var = "Hi i am a new file"
fp.write(var)
fp.close()

fp = open("vaibhav.txt","r+")
print(fp.read())
fp.close()

