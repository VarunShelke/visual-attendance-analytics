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

def daytoc():
    h=[]
    s=[]
    dtoc=df.loc[:,['TOC_LEC','TOC']]
    c=dtoc['TOC_LEC'][0]+1
    dd.loc[:, "TOC_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc) 
    for i in range(l):
        h.append(df['TOC'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "TOC%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
        
def daydbms():
    h=[]
    s=[]
    dtoc=df.loc[:,['DBMS_LEC','DBMS']]
    c=dtoc['DBMS_LEC'][0]+1
    dd.loc[:, "DBMS_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc)
    for i in range(l):
        h.append(dtoc['DBMS'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "DBMS%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
        
def dayisee():
    h=[]
    s=[]
    dtoc=df.loc[:,['ISEE_LEC','ISEE']]
    c=dtoc['ISEE_LEC'][0]+1
    dd.loc[:, "ISEE_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc)
    for i in range(l):
        h.append(dtoc['ISEE'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "ISEE%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
    
def daysepm():
    h=[]
    s=[]
    dtoc=df.loc[:,['SEPM_LEC','SEPM']]
    c=dtoc['SEPM_LEC'][0]+1
    dd.loc[:, "SEPM_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc)
    for i in range(l):
        h.append(dtoc['SEPM'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "SEPM%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
     
def daycn():
    h=[]
    s=[]
    dtoc=df.loc[:,['CN_LEC','CN']]
    c=dtoc['CN_LEC'][0]+1
    dd.loc[:, "CN_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc)
    for i in range(l):
        h.append(dtoc['CN'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "CN%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
    
def daysdl():
    h=[]
    s=[]
    dtoc=df.loc[:,['SDL_LEC','SDL']]
    c=dtoc['SDL_LEC'][0]+1
    dd.loc[:, "SDL_LEC"]=c
    dd.to_csv("TE2.csv", index=False)
    d=df['TOC_LEC'][0]+df['DBMS_LEC'][0]+df['ISEE_LEC'][0]+df['SEPM_LEC'][0]+df['CN_LEC'][0]+df['SDL_LEC'][0] 
    l=len(dtoc)
    for i in range(l):
        h.append(dtoc['SDL'][i])
    for i in range(l):
        a=(h[i]/c)*100
        s.append("%.2f" % round(a,2))
    a=305101
    for i in range(l):
        dd.loc[dd["Roll No."]==a, "SDL%"]=s[i] 
        a=a+1
        dd.to_csv("TE2.csv",index=False)
    total(d)
    
def mon():
    dd.loc[:,"ISEE_STAT"]='A'
    dd.loc[:,"TOC_STAT"]='A'
    dd.to_csv("TE2.csv",index=False)
    dayisee()
    daytoc()
    
def tue():
    dd.loc[:,"TOC_STAT"]='A'
    dd.loc[:,"ISEE_STAT"]='A'
    dd.loc[:,"SDL_STAT"]='A'
    dd.loc[:,"DBMS_STAT"]='A'
    dd.loc[:,"CN_STAT"]='A'
    dd.to_csv("TE2.csv",index=False)
    daytoc()
    dayisee()
    daysdl()
    daydbms()
    daycn()
    
def wed():
    dd.loc[:,"SEPM_STAT"]='A'
    dd.loc[:,"DBMS_STAT"]='A'
    dd.loc[:,"TOC_STAT"]='A'
    dd.loc[:,"CN_STAT"]='A'
    dd.loc[:,"ISEE_STAT"]='A'
    dd.to_csv("TE2.csv",index=False)
    daysepm()
    daydbms()
    daytoc()
    daycn()
    dayisee()
    
def thurs():
    dd.loc[:,"SEPM_STAT"]='A'
    dd.loc[:,"DBMS_STAT"]='A'
    dd.loc[:,"CN_STAT"]='A'
    dd.to_csv("TE2.csv",index=False)
    daysepm()
    daydbms()
    daycn()
    
def fri():
    dd.loc[:,"CN_STAT"]='A'
    dd.loc[:,"SEPM_STAT"]='A'
    dd.loc[:,"TOC_STAT"]='A'
    dd.loc[:,"SDL_STAT"]='A'
    dd.to_csv("TE2.csv",index=False)
    daycn()
    daysepm()
    daytoc()
    daysdl()
    
def dayforA(b):
    a=b.upper()
    if a=='MONDAY':
        mon()
    elif a=='TUESDAY':
        tue()
    elif a=='WEDNESDAY':
        wed()
    elif a=='THURSDAY':
        thurs()
    elif a=='FRIDAY':
        fri()
    else:
        print('Incorrect input')
    