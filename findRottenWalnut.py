import sys

def main():
    List = [1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 1, 1,]
    size = len(List)
    
    print "List:", List
    print "List size:", size
    index = findRottenWalnut(List, size)
    print "index of different element is", index


def findRottenWalnut(List, size):
    if size < 1:
        return -1
    elif size == 1:
        return 0;
    elif size == 2:
        if List[0]<List[1]:
            return 0;
        else:
            return 1;
    else:
        #listeyi ikiye ayirdim
        halfSize = size/2
        leftList = List[:halfSize] #ilk yarisini alir
        rightList = List[halfSize:] #ikinci yarisini alir
        
        result = compareScales(leftList, rightList)
        if result == -1: #result neagatif ise rotten walnut sag listededir
            return halfSize + findRottenWalnut(rightList, len(rightList)) 
            #saga gidildiginde left'in eleman sayisi kadar index atlanmis 
            #olacagi icin halfSize ile toplama yapildi
        elif result == 1: #result pozitif ise rotten walnut sol listededir
            return findRottenWalnut(leftList, len(leftList))
        else: #result 0 ise rotten walnut yoktur
            return -1


#listedeki elemanlarin toplaminin listenin boyutuna bolumu birim basina 
#dusen agiriligi verecegi icin size'a bolmeyi ekledim. 
#birim basina dusen agirlik left de daha kucuk ise -1
#birim basina dusen agirlik right ta daha kucuk ise 1
#birim basina dusen agirliklar esit ise 0 return edildi. 
def compareScales (leftScaleList, rightScaleList):
    result = sum(leftScaleList)/len(leftScaleList) - sum(rightScaleList)/len(rightScaleList)
    if result < 0:
        return 1
    elif result > 0:
        return -1
    else:
        return 0
        

#Bu dosya calistirildginda calistirilacak fonksiyon belirtildi        
if __name__ == "__main__":
    main()
