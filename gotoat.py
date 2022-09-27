import datetime
import atstud
a=datetime.time(8,45,0,0)
b=datetime.time(9,45,0,0)
c=datetime.time(10,45,0,0)
d=datetime.time(11,0,0,0)
e=datetime.time(12,0,0,0)
f=datetime.time(13,0,0,0)
g=datetime.time(14,0,0,0)
h=datetime.time(15,0,0,0)
i=datetime.time(16,0,0,0)
j=datetime.time(17,0,0,0)

def atmon(n,r):
    if n>a and n<b:
        atstud.atisee(r)
    elif n>b and n<c:
        atstud.attoc(r)
    else:
        print("Now there is no lecture going!!!")
        
def attues(n,r):
    if n>d and n<e:
        atstud.attoc(r)
    elif n>e and n<f:
        atstud.atisee(r)
    elif n>g and n<h:
        atstud.atsdl(r)
    elif n>h and n<i:
        atstud.atdbms(r)
    elif n>i and n<j:
        atstud.atcn(r)
    else:
        print("Now there is no lecture going!!!")
        
def atwed(n,r):
    if n>d and n<e:
        atstud.atsepm(r)
    elif n>e and n<f:
        atstud.atdbms(r)
    elif n>g and n<h:
        atstud.atcn(r)
    elif n>h and n<i:
        atstud.attoc(r)
    elif n>i and n<j:
        atstud.atisee(r)
    else:
        print("Now there is no lecture going!!!")
        
def atthurs(n,r):
    if n>g and n<h:
        atstud.atsepm(r)
    elif n>h and n<i:
        atstud.atdbms(r)
    elif n>i and n<j:
        atstud.atcn(r)
    else:
        print("Now there is no lecture going!!!")
        
def atfri(n,r):
    if n>a and n<b:
        atstud.atcn(r)
    elif n>b and n<c:
        atstud.atsepm(r)
    elif n>d and n<e:
        atstud.atsdl(r)
    elif n>e and n<f:
        atstud.attoc(r)
    else:
        print("Now there is no lecture going!!!")
        
def gtat(d,n,r):
    a=d.upper()
    if a=='MONDAY':
        atmon(n,r)
    elif a=='TUESDAY':
        attues(n,r)
    elif a=='WEDNESDAY':
        atwed(n,r)
    elif a=='THURSDAY':
        atthurs(n,r)
    elif a=='FRIDAY':
        atfri(n,r)
    else:
        print('Incorrect input')