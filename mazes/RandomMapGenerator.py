# Makes random maps
# ------------------
import random,queue

wall="."
up="^"
lt="<"
dn="V"
rt=">"
path="+"

print("The default filename is default.txt")
filename=input("What would you like to call the map? ")

themap=[]

height = 40
width = 80

sp=0.075

# make a map
themap.append([wall]*(width))
for k in range(1,height-1):
    themap.append([wall]+ list(" "*(width-2)) + [wall])
themap.append(list(wall*(width)))

cont=20
rep=15

k=0
for k in range(1,cont):
    i= random.randint(5, height-5)
    j= random.randint(5, width-5)

    themap[i][j]=str(k)


    

for k in range(rep,1,-1):
    for i in range(1,height-1):
        for j in range(1,width-1):
            sway=0
            s=[]
            for ip in [i-1,i,i+1]:
                for jp in [j-1,j,j+1]:
                    if ((themap[ip][jp])!=" "):
                        s=s+[themap[ip][jp]]
                        sway=sway+sp
            
            if (random.random() < sway) and (len(set(s))==1):
               themap[i][j]=s[0]


count=0
# count the white spaces
for i in range(1,height-1):
    for j in range(1,width-1):
        if (themap[i][j]==" "):
            count=count+1
                
# randomly choose a start
s=random.randint(1, count-1)

count=0
for i in range(1,height-1):
    for j in range(1,width-1):
        if (themap[i][j]==" "):
            count=count+1
            if (count==s):
                themap[i][j]="S"


#Find the start
for x in range(0,height):
    for y in range(0,width):
        if themap[x][y]=="S": i=x;j=y
                
q=queue.Queue()

# look in all directions
if (i>0): q.put([i-1,j,dn])
if (i<height-1): q.put([i+1,j,up])
if (j>0): q.put([i,j-1,rt])
if (j<width-1): q.put([i,j+1,lt])

fi=-1
fj=-1
success=False


while(not (q.empty())):
    [i,j,d] = q.get() # find the next place to look
    # check if it is unexplored (" ")
    if (themap[i][j]==" "):
        # write down where you came from
        themap[i][j]=d
        # look in all directions
        if (i>0): q.put([i-1,j,dn])
        if (i<height-1): q.put([i+1,j,up])
        if (j>0): q.put([i,j-1,rt])
        if (j<width-1): q.put([i,j+1,lt])


themap[i][j]="F"


#check the filename
filename = filename.split(".")[0]
if not (filename.isalnum() and len(filename)>0):
    filename="default"
filename=filename+".txt"


f = open(filename, "w")

for row in themap:
    r=""
    for e in row:
        if (e==" " or e=="S" or e=="F"):
            r=r+e
        elif (e.isdigit() or e==wall):
           r=r+wall
        else:
           r=r+" "
    f.write(r + "\n")
    print(str(r))

f.close()

print(" ")
print("The output is " + filename)


 
