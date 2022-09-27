import pandas as pd
import matplotlib.pyplot as mp

def plottable(sn,nlp,lper,a):
    dis=pd.DataFrame([sn,nlp,lper]).T
    dis.rename(index=str,columns={0:'Subject Name',1:'No. of lectures attended',2:'Attendance in Percentage'},inplace=True)
    fig,ax=mp.subplots()
    colW=[2/6,2/6,2/6]
    mp.axis('off')
    ax.table(cellText=dis.values,colLabels=dis.columns,loc='center',cellLoc='center',colWidths=colW).scale(2,2)
    mp.title(int(a))
    mp.show()
    
def studAtten(a):
    if int(a)>305100 and int(a)<305199:
        dd=pd.read_csv("TE2.csv")
        df=dd.loc[:,:]
        rv=df[df['Roll No.']==int(a)]
        #print('Roll NO.:',int(rv['Roll No.']))
        sn=['TOC','DBMS','SEPM','ISEE','CN','SDL','TOTAL']
        nlp=[int(rv.TOC),int(rv.DBMS),int(rv.SEPM),int(rv.ISEE),int(rv.CN),int(rv.SDL),int(rv.Total)]
        lper=[float(rv['TOC%']),float(rv['DBMS%']),float(rv['SEPM%']),float(rv['ISEE%']),float(rv['CN%']),float(rv['SDL%'])
              ,float(rv['Total%'])]
        plottable(sn,nlp,lper,a)
    else:
        print("There is no such roll number!!!")
    