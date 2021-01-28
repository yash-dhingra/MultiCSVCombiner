import csv 
import os
import shutil

src_dir = os.getcwd()
name=1
listofcsv=os.listdir("CSV")
print(listofcsv)
dest_dir="Temp"
for i in listofcsv:
    src_file = os.path.join(src_dir,"CSV", i)
    shutil.copy(src_file,dest_dir)
    dst_file=os.path.join(dest_dir,str(i))
    new_dst_file_name = os.path.join(dest_dir, str(str(name)+".csv"))
    os.rename(dst_file, new_dst_file_name)
    name+=1

nm=dict()

#Not Required...
'''y=int(input("Enter The Number of Files: "))
filenames=[] 
filenames2=[]
for i in range (2,y+1):
    filenames.append(i)
for i in range (1,y+1):
    filenames2.append(i)
'''

#here = os.path.dirname(os.path.abspath(__file__))
here=dest_dir
filenames=[]
for i in range (2,len(listofcsv)):
    filenames.append(i)

filename1 = os.path.join(here,"1.csv")

n=0
with open (filename1,'rt') as f:
    csv1=csv.reader(f)
    for row in csv1:
        n+=1
        if n==1:
            print(row)
            markscolumn=int(input("Which Column has the total Marks?: "))-1
            continue
        nm[row[1]]=[str(row[markscolumn]),]
temp_dir=os.listdir("Temp")
#print(temp_dir)
temp_dir.remove("1.csv")
for i in temp_dir:
    n=0
    print(i)
    i=os.path.join("Temp",i)
    with open (i,'rt') as tf:
        tobject=csv.reader(tf)
        for row in tobject:
            n+=1
            if n==1:
                continue
            a=[]
            try:
                a=nm[row[1]]
                print("chal pda")
            except:
                nm[row[1]]=a
            a.append(str(row[markscolumn]))

keyslist=list(nm.keys())
subjects=["Name", ]

finalcsv=os.path.join(src_dir,"final.csv")

with open (finalcsv,mode="w") as final:
    finalfile = csv.writer(final, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    subjects=subjects+listofcsv

    finalfile.writerow(subjects)
    for i in keyslist:
        a=nm[i]
        b=[i,]
        for u in a:
            b.append(u)
        finalfile.writerow(b) 
print(nm)