def merge_the_tools(s, k):
    print('\n'.join([''.join(list(dict.fromkeys(item))) for item in [s[k*i:k*(i+1)] for i in range(len(s)//k)]]))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
