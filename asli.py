import sys
import urllib.request
from urllib.parse import urlparse
class check(object):
    def __init__(self):pass
    def address(self):
        add=input("Enter URL Address With HTTP to Send Data: \n")
        if add:
            o = urlparse(add)
            if not o.scheme:
                self.address()
            else:
                self.address=add
        else:
            self.address()
    def method(self):
        method=input("Enter Method Name (GET OR POST) \n")
        if method:
            if method=="POST" or method=="post" or method=="get" or method=="GET":
                self.method=method
            else:
                self.method()
        else:
             self.method()
    def getkey(self):
        keys=input("Enter Key's To Send exam: name,family,number \n")
        if not len(keys):
            self.getkey()
        else:
            keys=keys.split(',')
            self.keys=keys
    def getval(self):
        values=input("Enter values's To Send exam saeid,ahmadi,2 \n")
        if not len(values):
            self.getval()
        else:
            values=values.split(',')
            self.values=values   
    def post_(self,address,**datas):
        data = urllib.parse.urlencode(datas)
        data = data.encode('utf-8')
        request = urllib.request.Request(address)
        request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
        request.add_header("User-Agent","Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
        try :
            f = urllib.request.urlopen(request, data)
            print("Response Recived From "+address+" : \n")
            print(f.read().decode('utf-8'))
            again=input("Do you want to test again ? yes or no")
            if again=='yes':
                main()
            else:
                sys.exit(0)
        except urllib.error.URLError as err0:
            print(err0)
        except urllib.error.HTTPError as err1:
            print(err1)
    def get_(self,address):
        request = urllib.request.Request(address)
        request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
        request.add_header("User-Agent","Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
        request.add_header('Referer', 'http://www.python.org/')
        try :
            f = urllib.request.urlopen(request)
            print("Response Recived From "+address+" : \n")
            print(f.read().decode('utf-8'))
            again=input("Do you want to test again ? yes or no")
            if again=='yes':
                main()
            else:
                sys.exit(0)
        except urllib.error.URLError as err0:
            print(err0)
        except urllib.error.HTTPError as err1:
            print(err1)
        
def main():
    barname=check()
    barname.address()
    barname.method()
    barname.getkey()
    barname.getval()
    address=barname.address
    method=barname.method
    key=barname.keys
    val=barname.values

    if method=="GET" or method=="get" :
        c=0
        datas={}
        for i in key:
            datas[i]=val[c]
            c=c+1
        datass=str(datas)
        a=datass.replace('}','')
        a=a.replace('{','')
        a=a.replace("'",'')
        a=a.replace(":",'=')
        a=a.replace(",",'&')
        a=a.replace(" ",'')
        j=address+'?'+a
        barname.get_(j)
    else:
        c=0
        datas={}
        for i in key:
            datas[i]=val[c]
            c=c+1
        barname.post_(address,**datas)
if __name__=="__main__":main()
