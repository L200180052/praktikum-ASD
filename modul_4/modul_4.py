import mahasiswa as mhs

c1=mhs.mhsTIF("ino",21,"solo",240000)
c2=mhs.mhsTIF("iso",23,"klaten",220000)
c3=mhs.mhsTIF("ido",21,"jogja",260000)
c4=mhs.mhsTIF("iwo",24,"klaten",250000)
c5=mhs.mhsTIF("ifo",26,"magelang",240000)
c6=mhs.mhsTIF("ibo",21,"jakarta",250000)
c7=mhs.mhsTIF("iko",23,"solo",220000)

x = [c1, c2, c3, c4, c5, c5, c6, c7]
#nomer 1
def cari(x,a):
    aa=[]
    for i in x:
        if i.Nama == a:
            aa.append(x.index(i))
        elif i.uang == a:
            aa.append(x.index(i))
        elif i.kota == a:
            aa.append(x.index(i))
        elif i.NIM == a:
            aa.append(x.index(i))
    return aa

print(cari(x,21))

#nomer 2
def kecil(x):
    minim = x[0].uang
    for i in x:
        if i.uang < minim:
            minim = i.uang
    return minim

print(kecil(x))

#nomer 3
def kecil1(x):
    minim = x[0].uang
    a = []
    for i in x:
        if i.uang < minim:
            minim = i.uang
    for i in x:
        if i.uang == minim:
             a.append(i.Nama)
    return a

print(kecil1(x))

#nomer 4
def kurang(x):
    a=[]
    for i in x:
        if i.uang < 250000:
            a.append(i.Nama)
    return a
print(kurang(x))

#nomer 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    #fungsi untuk menambah
    def addhead(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return self.head
    def cari(self,x):
        position=0
        node=self.head
        while node is not None:
            position+=1
            if node.data == x:
                print (node.data," di posisi:",position)
                break
            else:
                node = node.next

a=LinkedList()
a.addhead(12)
a.addhead(23)
a.addhead(45)
a.addhead(32)
a.addhead(89)
a.addhead(27)
a.addhead(47)
a.cari(23)


#nomer 6
def binSe(list, target):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            return "target di index:",list.index(target)
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid +1
    return False

list = [2,4,6,9,12,27,39,46,59,77]
target = 12
print(binSe(list,target))
list = [2,4,6,9,12,27,39,46,59,77]
target = 133
print(binSe(list,target))

#nomer 7
def binSe(list, target):
    a=[]
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            a.append(list.index(target))
            i=list.index(target)-1
            j = list.index(target) + 1
            while target == list[i]:
                a.append(i)
                i-=1
            while target == list[j]:
                a.append(j)
                j+=1
            return a
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return "target tidak ditemukan di index berapapun"

list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(list,target))
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(list,target))


#8
