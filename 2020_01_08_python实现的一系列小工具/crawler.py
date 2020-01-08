import urllib
import re
import pprint

x = 1

def printUrl(index):
    object = urllib.urlopen( 'http://tieba.baidu.com/p/2460150866?pn=' + str(index) )
    source = object.read()

    compiled_regex = re.compile(r'src="(.+?\...g)" pic_ext')
    image_urls = re.findall(compiled_regex, source)
    
    a = 0
    for i in image_urls:
        if 'http://tb2.bdstatic.com/tb/static-pb/img/head_80.jpg' in i:
            image_urls.pop(a)
        if len(i) > 325:
            image_urls.pop(a)
        a += 1
    print 'The pictures count are: ' + str(a)
    
    global x
    for i in image_urls:
        urllib.urlretrieve(i, '%s.jpg' % x)
        x += 1    

def main():
    for i in range(1, 75):
        printUrl(i)

if __name__ == '__main__':
    main()
