from itertools import count
from logging import exception
from tkinter.messagebox import NO


class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next


class LinkedList:
    def __init__(self):
        self.head=None


    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head=node
        return

    def print(self):
        itr=self.head
        llist=[]
        while itr:
            llist.append(str(itr.data))
            itr=itr.next
        print(llist)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next
        return count    

    def insert_at_end(self,data):  
        if self.head==None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
           itr=itr.next    

        itr.next=Node(data)   

    def insert_at(self,index,data):
        if index<0 or index > self.get_length():
            raise exception("Invalid Index")
        elif index==0:
            self.insert_at_begining(data)    
            return
        itr=self.head  
        count=0  
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    
    
    def remove(self,index):
        if index<0 or index > self.get_length():
            raise exception("Invalid Index")
        if index==0:
            self.head=self.head.next  
            return

        itr=self.head  
        count=0  
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1        

    def insert_in_bulk(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)    



l1=LinkedList()
l1.insert_at_begining(10)  
l1.insert_at_end(40)
l1.print()        
print(l1.get_length())
l1.insert_at(1,24)
l1.print()
l1.remove(1)
l1.insert_in_bulk([1,2,3])
l1.print()
