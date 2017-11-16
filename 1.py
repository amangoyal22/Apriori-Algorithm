import xlrd


def Apriori():
    each()
    listprep()
    list2()
    clear3()
    list3()
    tableone()
    tabletwo()
    clear()
def each():
    k=len(data)
    for i in data:
        x=0
        for j in data[i]:
           x+=j
        if(x>=minsupport):
            support[i]=x
    print("L1 = >",support)
def listprep():
    y=[]
    for i in support:
        y.append(i)
        for j in support:
            if i is not j:
                x=[i,j]
                if j not in y:
                    c2.append(x)
    print("c2 = > ",c2)
def list2():
    y=0
    for j in c2:
        k=[j]
        x=0
        for i in range(0,len(data[j[0]])):
          x+=data[j[0]][i]*data[j[1]][i]
        k.append(x)
        if x >= minsupport:
            L2[y]=k
            y+=1
    print("L2 = > ",L2)
def clear3():
    y=[]
    for i in L2:
        y.append(L2[i][0])
        for j in L2:
            if L2[j][0] not in y:
                k=L2[i][0]
                l=L2[j][0]
                if set(k) & set(l):
                    x=[]
                    for i in set(k) | set(l):
                        x.append(i)
                    C3.append(x)
    print("C3 = > ",C3)
def list3():
    for i in C3:
        k=0
        y=[i]
        x=0
        for j in range(0,len(data[i[0]])):
            x += data[i[0]][j] * data[i[1]][j]* data[i[2]][j]
        y.append(x)
        L3[k]=y
    print("L3 = > ",L3)
def tableone():
    for i in L3:
        arr=L3[i][0]
        spprt=L3[i][1]
        x=[]
        for  j in range(0,len(arr)):
            x.append(arr[j])
            for k in arr:
                if k not in x:
                    a=[arr[j],k]
                    b=arr
                    y=set(b)-set(a)
                    r=[]
                    for q in y:
                        r.append(q)
                    C4.append([[arr[j],k],[q],spprt])
                    C4.append([[q],[arr[j],k],spprt])
    print("C4 = >",C4)
def tabletwo():
    y = 0
    for i in C4:
        x=0
        j=i[0]
        if(len(j)>1):
            for k in range(0, len(data[j[0]])):
                x += data[j[0]][k] * data[j[1]][k]
            C4[y].append(i[2]/x)
            y=y+1
        if (len(j) == 1):
            for k in range(0, len(data[j[0]])):
                x += data[j[0]][k]
            C4[y].append(i[2]/x)
            y=y+1
    print("C4 with condidence",C4)
def clear():
    print("results(with 85% or greater) => ")
    for i in C4:
        if(i[3]>= minconf):
            RESULT.append([i[0],i[1]])
            print("\t",i[0]," => ",i[1])



if __name__ == "__main__":
    data = {}
    support = {}
    c2 = []
    L2 = {}
    C3 = []
    L3 = {}
    C4 = []
    RESULT = []
    minsupport = 63 * 8 / 100
    minconf = 85 / 100
    print("MINSUPPORT ==> ", minsupport)
    print("MINCONFIDENCE ==> ", minconf)
    file_location = "1.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    attribute = sheet.ncols
    di = sheet.nrows
    for i in range(0, attribute):
        data[sheet.cell_value(0, i)] = []
        for j in range(1,di):
            data[sheet.cell_value(0, i)].append(sheet.cell_value(j, i))
    print("DATASET = > ", data)
    Apriori()