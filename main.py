import os
origin = "**PLACE HERE YOUR DIR**"

# Open Folder
print(len(os.listdir(origin)))

# Open the File
with open("FILES.txt", mode="w") as file:
    # For each file:
    for f in os.listdir(origin):

        # Read the files | and formating
        f = f.replace("_", " ").replace("-", " - ").title()
        print(f[:f.index(".")])
        file.write(f[:f.index(".")] + "\n")
        
