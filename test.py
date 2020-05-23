import glob
files = glob.glob('./songs/*')
print(len(files))

for file in files:
    f = open(file+'/lyrics.txt')
    #print(file)
    Allf = f.read()
    text = Allf.replace('\n','')
    text = text.replace('\r','')
    #print(text, end ="")
