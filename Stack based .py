
# coding: utf-8

# In[30]:


#Stack implementation
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


# In[50]:


#Parenthesis Checker
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def par_checker(symbol_string):
    s=Stack()
    balanced=True
    index=0
    while(index<len(symbol_string) and balanced):
        symbol=symbol_string[index]
        if(symbol=='('):
            s.push(symbol)
        elif(s.is_empty()):
            balanced=False
        else:
            s.pop()
        index=index+1
    if(balanced and s.is_empty()):
        return True
    else:
        return False
symbol_string='(()'
print(par_checker(symbol_string))


# In[60]:


#decimal to any base converter
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
def base_converter(deci_number,base):
    digits="0123456789ABCDEF"
    rem_stack=Stack()
    while(deci_number>0):
        rem=deci_number%base
        rem_stack.push(rem)
        deci_number=deci_number//base
    n_string=""
    while(rem_stack.is_empty()==False):
        n_string=n_string+digits[rem_stack.pop()]
    return n_string
print(base_converter(34,2))
print(base_converter(34,10))
print(base_converter(34,8))
print(base_converter(34,16))

