class uraiRajutKata:
    def urai(self,kata):
        for i in range(len(kata)):
            for j in range(i+1):
                print(kata[j],end="")
    def rajut(self,kata):
        pjgKata=len(kata)
        listKata=list(kata)
        count=0
        hapus=0
        kataBaru=""
        while pjgKata>0:
            pjgKata=pjgKata-count
            count+=1
        for i in range(count-2):
            for j in range(i+1):
                listKata.remove(listKata[j])
        for i in listKata:
            kataBaru+=i
            print(kataBaru)
    # rajut("CCoCodCode")

x = uraiRajutKata()
x.urai("Code")
x.rajut("CCoCodCode")