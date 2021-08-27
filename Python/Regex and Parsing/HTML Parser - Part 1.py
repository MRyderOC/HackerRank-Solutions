from html.parser import HTMLParser


class HackerRankHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        if attrs:
            for item in attrs:
                print(f'-> {item[0]} > {item[1]}')
    
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
    
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        if attrs:
            for item in attrs:
                print(f'-> {item[0]} > {item[1]}')
    

parser = HackerRankHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))
parser.close()
