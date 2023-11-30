import random
#creat class for client
class Ponque :
    #count for caleculate how many client 
    _count = 0
    def __init__(self , n_client , n_compte , sold  , password=(random.randint(100, 999)) , cin="EE4576" ) :
        self.__n_client = n_client
        self.__n_comte = n_compte
        self.__sold = sold
        self.__password = password
        self.cin = cin 
        Ponque._count += 1
    
    def get_sold(self):
        return self.__sold
    
    #creat method for Deposit money in usd
    
    def deposit_money(self,n_money):
        if n_money>0 :
            return self.__sold + n_money
        else :
            print("try agin")
        
    def nclient(self):
        self.__n_client = Ponque._count
    
    #creat method for withdraw money
    
    def withdraw_money(self,w_sold) :
        return self.__sold -  w_sold 
    
    #change pass worrld
    
    def set_p_w(self, new_p_w) :
        if len(new_p_w)>5 :
           self.__password = new_p_w 
        else :
           ('try agin this password no valid ')
#fonction for ceate compte
    # def creat_compte(self,cin):
    #     if cin == self.__cin :
    #          print("sorry this count is existe;")
    #     else :
    #         print(f"welcome we are at your servic your sold is{self.__sold} and your number of your compte is{self.__n_comte} your password {self.__password} change your passworld before 24h")
     
    def delete_compte(self):
         del self.__n_comte
         Ponque._count -= 1 
    def info_client(self) :
        return [{self.__n_comte:self.__sold,},{self.__n_client : self.__password} , {self.__n_client : self.__n_comte}]
    def n_compte(self):
        rt=(random.randint(100, 999))
        return [ [int(digit) for digit in str(Ponque)]+int(digit) for digit in str(rt)]
class Agent_Bonque(Ponque) :
    def __init__(self , n_client ,  n_compte , sold , password ) :
        super.__init(n_client , n_compte , sold , password) 
    def newcompte(self , n_client , n_compte  , sold, password ):
        self.__n_client= n_client
        self.__n_comte = n_compte
        self.__sold = sold
        self.__password= password
    def delete_compte(self):
        return super().delete_compte()
    def deposit_money(self, n_money):
        return super().deposit_money(n_money)
    def withdraw_money(self, w_sold):
        return super().withdraw_money(w_sold)
    def get_sold(self):
        return super().get_sold()
    def set_p_w(self, new_p_w):
        return super().set_p_w(new_p_w)
     