import pandas as pd

dd=pd.read_csv("TE2.csv")
df=dd.loc[:,:]

def total(d):
    toc=[]
    dbms=[]
    isee=[]
    sepm=[]
    cn=[]
    sdl=[]
    total_per=[]
    total=[]
    l=len(df)
    for i in range(l):
        toc.append(df['TOC'][i])
        dbms.append(df['DBMS'][i])
        isee.append(df['ISEE'][i])
        sepm.append(df['SEPM'][i])
        cn.append(df['CN'][i])
        sdl.append(df['SDL'][i])
    for i in range(l):
        sum=0
        sum=toc[i]+dbms[i]+isee[i]+sepm[i]+cn[i]+sdl[i]
        t=(sum/d)*100
        total.append(sum)
        total_per.append("%.2f" % round(t,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "Total%"]=total_per[i] 
        dd.loc[dd["Roll No."]==a, "Total"]=total[i]
        a=a+1
        dd.to_csv("TE2.csv",index=False)
        
def attoc(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['TOC_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.TOC)+1
        c=float(rv.TOC_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "TOC"]=b
        dd.loc[dd["Roll No."]==int(a), "TOC%"]=e
        dd.loc[dd["Roll No."]==int(a), "TOC_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("Nothing")
   
    
def atdbms(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['DBMS_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.DBMS)+1
        c=float(rv.DBMS_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "DBMS"]=b
        dd.loc[dd["Roll No."]==int(a), "DBMS%"]=e
        dd.loc[dd["Roll No."]==int(a), "DBMS_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("Nothing")
    
def atisee(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['ISEE_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.ISEE)+1
        c=float(rv.ISEE_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "ISEE"]=b
        dd.loc[dd["Roll No."]==int(a), "ISEE%"]=e
        dd.loc[dd["Roll No."]==int(a), "ISEE_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("Nothing")
    
def atsepm(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['SEPM_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.SEPM)+1
        c=float(rv.SEPM_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "SEPM"]=b
        dd.loc[dd["Roll No."]==int(a), "SEPM%"]=e
        dd.loc[dd["Roll No."]==int(a), "SEPM_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("nothing")
    
def atcn(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['CN_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.CN)+1
        c=float(rv.CN_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "CN"]=b
        dd.loc[dd["Roll No."]==int(a), "CN%"]=e
        dd.loc[dd["Roll No."]==int(a), "CN_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("Nothing")
    
def atsdl(a):
    rv=df[df['Roll No.']==int(a)]
    p1='P'
    p3='A'
    k=int(rv['Sr. No.'])
    j=k-1
    p2=rv['SDL_STAT'][j]
    if p1==p2:
        print("Your presenty is marked already!!")
    elif p2==p3:
        b=int(rv.SDL)+1
        c=float(rv.SDL_LEC)
        d=b/c*100
        e="%.2f" % round(d,2)
        dd.loc[dd["Roll No."]==int(a), "SDL"]=b
        dd.loc[dd["Roll No."]==int(a), "SDL%"]=e
        dd.loc[dd["Roll No."]==int(a), "SDL_STAT"]='P'
        dd.to_csv("TE2.csv", index=False)
        d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0]
        total(d)
    else:
        print("Nothing")