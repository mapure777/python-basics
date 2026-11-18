# Create and Open file in write mode
file=open("example.txt","w")

# Write to the file
file.write("Hello, Ektoras\n")
file.write("This is a smaple file.")
file.write("how r u doing.")
# Close the file 
file.close()

# Open file in read mode
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()
print("File Content:\n" + content)
File = open("example.txt")

# Read the entire content of the file

content = file.read
