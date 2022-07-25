class Item: #Class
    def cal(x, y): #Function but inside class hence aka method | Each method/function need atleast 1 argument(call itself) aka self(convention)
        return x * y
item = Item() # Instance aka calling a function/method aka creating/initiating a object of a class
print(item.cal(1,2))