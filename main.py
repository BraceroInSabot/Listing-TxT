import os
origin = "C:\\Users\\guilh\\OneDrive\\Documentos\\Trabalho\\Blog_receitas_da_Graca\\graca_receitas\\receitas_feitas"

# Open Folder
print(len(os.listdir(origin)))

# Open the File
with open("receitas_feitas_Bracero.txt", mode="w") as file:
    # For each file:
    for f in os.listdir(origin):

        # Read the files | and formating
        f = f.replace("_", " ").replace("-", " - ").title()
        print(f[:f.index(".")])
        file.write(f[:f.index(".")] + "\n")
        
