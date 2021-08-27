from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        l = data.split('\n')
        if len(l) == 1:
            print(f'>>> Single-line Comment\n{l[0]}')
        else:
            print('>>> Multi-line Comment')
            for item in l:
                print(item)
    
    def handle_data(self, data):
        if data != '\n':
            print(f'>>> Data\n{data}')
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
