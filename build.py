# import os

# dir_name = "docs"    #path
# input_files_index = ["templates/top.html", "content/index.html", "templates/bottom.html"]     #input files
# file_index_out = "./index.html"     #choose a name for the output file
# file_output = os.path.join(dir_name, file_index_out)

# fout = open(file_output, 'w')

# for tempfile in input_files_index:
#     inputfile = os.path.join(dir_name, tempfile)
#     fin = open(inputfile, 'r')
    
#     for line in fin:
#         fout.write(line)
        
# fin.close()    
# fout.close()

index_filenames = ["templates/top.html", "content/index.html", "templates/bottom.html"] #Input file list
with open('docs/index.html', 'w') as outfile:
    for fname in index_filenames:
        with open(fname) as infile:
            outfile.write(infile.read()) #Output single file
index_filenames = ["templates/top.html", "content/portfolio.html", "templates/bottom.html"] #Input file list
with open('docs/portfolio.html', 'w') as outfile:
    for fname in index_filenames:
        with open(fname) as infile:
            outfile.write(infile.read()) #Output single file
index_filenames = ["templates/top.html", "content/about.html", "templates/bottom.html"] #Input file list
with open('docs/about.html', 'w') as outfile:
    for fname in index_filenames:
        with open(fname) as infile:
            outfile.write(infile.read()) #Output single file
index_filenames = ["templates/top.html", "content/contact.html", "templates/bottom.html"] #Input file list
with open('docs/contact.html', 'w') as outfile:
    for fname in index_filenames:
        with open(fname) as infile:
            outfile.write(infile.read()) #Output single file
