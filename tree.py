from ast import Not


class Node:
    def __init__(self,word = ''):
        self.word=word
        self.children=dict()
        self.endOfTxt = False

class Tree:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        current = self.root
        for i, char in enumerate(word): #noha
            #split 
            splitWord = word[0:i+1]
            if splitWord not in current.children: #check kol char in noha not exist in children of current node
                #insert char to child of node
                current.children[splitWord] = Node(splitWord)

                #print(current.children)     
            #update el current node
            current = current.children[splitWord]
        current.endOfTxt = True


    def search(self,word):
        current = self.root
        #split
        for i, char in enumerate(word):
            splitWord = word[0:i+1]
        #access childrens and check if char exist
            if splitWord in current.children:
               current = current.children[splitWord]

            else:
                print(word, 'IS not exist')
                return False

        if current.endOfTxt :
            return current.word
        else:
            return [key for key in current.children]
                


t= Tree()
t.insert('ahmed')
t.insert('ahndko')
print(t.search('a'))
