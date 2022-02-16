filename = "/tmp/output_1.txt"
resultfile = "/tmp/output_2.txt"
infile = open(filename, 'r') 
outfile = open(resultfile, 'w')
lines = infile.readlines() 
for line in lines:
    sline = line.split()
    if not sline[0].startswith("#"):
        len_sline = len(sline)
        for field in range(len_sline):
            if field==0:
                identfield=sline[field]+"                    "
                identfield=identfield[:20]
                identline=identfield
            elif field==1:
                identfield=sline[field]+"                    "
                identfield=identfield[:20]
                identline=identline+identfield
            elif field!=len_sline-1:
                identfield=sline[field]+"   "
                identline=identline+identfield
            elif field==len_sline-1:
                identfield=sline[field]
                identline=identline+identfield
        outfile.write(identline+"\n")

for line in lines:
    if line.startswith("#"):
        outfile.write(line)

infile.close()
outfile.close()
