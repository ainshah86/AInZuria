from random import randint

#paparan pada skrin pemain, pemain perlu menaip r untuk Rock, p untuk Paper dan s untuk Scissors
print("*****************************************************")
print("Hello!\nLet's play 'Rock, Paper and Scissors Game .")

#Arahan untuk keluar dari permainan, tekan Q untuk keluar
print("Press 'Q' at any time to exit")

#gelung while akan ulang selagi syarat benar
while True:
    
    #pemain perlu memasukkan pilihan sama ada r untuk rock , p untuk paper dan s untuk scissors
    player = input ("Rock (r), Paper (p) or Scissors (s)?")
    
    print("*****************************************************")
    
    #struktur kawalan pelbagai pilihan if else
    if(player=='Q'):
        
        #paparan sekiranya pemain memilih untuk keluar dari permainan
        print("Thank you! See you again!")
        
        #henti 
        break
    
    #sebaliknya paparan pilihan pemain dan komputer dipaparkan
    else:
        
        print(player, "vs", end=" ")
        
        #modul random randint (mula 1, tamat 3) ,pilihan secara rawak sama ada r=1, p=2, s=3
        chosen=randint(1,3)
        
        #gelung pilihan komputer
        #cetak pilihan komputer
        #jika pilihan komputer adalah 1=r
        if chosen==1:
            computer="r"
            
        #jika pilihan komputer adalah 2=p
        elif chosen==2:
            computer="p"
            
        #sebaliknya pilihan komputer 3=s
        else:
            computer="s"
            
        #cetak pilihan komputer dalam string
        print(computer)
        
         #struktur kawalan pelbagai pilihan yang membandingkan pilihan pemain dengan komputer
        #jika pilihan sama
        if player==computer:
            
            #mencetak perkataan DRAW! pada skrin 
            print("DRAW!")
            
        #jika pilihan pemain=r dan pilihan komputer=s
        elif player=="r" or "R" and computer=="s":
            
            #mencetak perkataan Player wins!  pada skrin
            print("Player wins!")
            
        #jika pilihan pemain=r dan pilihan komputer=p
        elif player=="r" or "R" and computer=="p":
            
            #mencetak perkataan Computer wins!  pada skrin
            print("Computer wins!")
            
        #jika pilihan pemain=p dan pilihan komputer=r
        elif player=="p" or "P" and computer=="r":
            
            #mencetak perkataan Computer wins!  pada skrin 
            print("Computer wins!")
        
        #jika pilihan pemain=p dan pilihan komputer=s
        elif player=="p" or "P" and computer=="s":
            
            #mencetak perkataan Computer wins!  pada skrin
            print("Computer wins!")

        #jika pilihan pemain=s dan pilihan komputer=p
        elif player=="s" or "S" and computer=="p":
            
            #mencetak perkataan Player wins!  pada skrin
            print("Player wins!")
        
        #jika pilihan pemain=s dan pilihan komputer=r
        elif player=="s" or "S" and computer=="r":
            
            #mencetak perkataan Player wins!  pada skrin
            print("Player wins!")
            
