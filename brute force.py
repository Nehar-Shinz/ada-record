def search(pat,txt):
    M=len(pat)
    N=len(txt)
    found=0
    for i in range(N-M+1):
        j=0
        while(j<M):
            if(txt[i+j]!=pat[j]):
                break
            j+=1
        if(j==M):
            print("Pattern found at index",i)
            found=1
    if(found==0):
        print("Pattern not found")
pat1=input("Enter the pattern")
txt1=input("Enter the text")
search(pat1,txt1)