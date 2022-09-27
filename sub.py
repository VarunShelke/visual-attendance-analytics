import pandas as pd
import matplotlib.pyplot as mp

dd=pd.read_csv("TE2.csv")
df=dd.loc[:,:]

def TOC():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','TOC','TOC%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:TOC' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.TOC[i])
    for i in range(l):
        e.append(dtoc['TOC%'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'TOC lecture Attended',3:'% of TOC Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def DBMS():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','DBMS','DBMS%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:DBMS' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.DBMS[i])
    for i in range(l):
        e.append(dtoc['DBMS%'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'DBMS lecture Attended',3:'% of DBMS Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def SEPM():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','SEPM','SEPM%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:SEPM' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.SEPM[i])
    for i in range(l):
        e.append(dtoc['SEPM%'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'SEPM lecture Attended',3:'% of SEPM Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def ISEE():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','ISEE','ISEE%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:ISEE' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.ISEE[i])
    for i in range(l):
        e.append(dtoc['ISEE%'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'ISEE lecture Attended',3:'% of ISEE Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def CN():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','CN','CN%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:CN' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.CN[i])
    for i in range(l):
        e.append(dtoc['CN'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'CN lecture Attended',3:'% of CN Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def SDL():
    q=[]
    w=[]
    r=[]
    e=[]
    dtoc=df.loc[:,['Roll No.','Name','SDL','SDL%']]
    print('\t\t\t\t\t\t\t\b\033[1m' + 'Subject:SDL' + '\033[0m')
    l=len(dtoc)
    for i in range(l):
        q.append(dtoc['Roll No.'][i])
    for i in range(l):
        w.append(dtoc.Name[i])
    for i in range(l):
        r.append(dtoc.SDL[i])
    for i in range(l):
        e.append(dtoc['SDL%'][i])
    dis=pd.DataFrame([q,w,r,e]).T
    dis.rename(index=str,columns={0:'Roll NO.',1:'Name',2:'SDL lecture Attended',3:'% of SDL Attendance'},inplace=True)
    fig,ax=mp.subplots()
    colW=[0.15,0.55,0.15,0.15]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(3,3)
    mp.show()
    
def subwise(b):
    a=b.upper()
    if a=='TOC':
        TOC()
    elif a=='DBMS':
        DBMS()
    elif a=='SEPM':
        SEPM()
    elif a=='ISEE':
        ISEE()
    elif a=='CN':
        CN()
    elif a=='SDL':
        SDL()
    else:
        print('Incorrect input')