from string import ascii_lowercase, ascii_uppercase

def swap_case(s):
    swap_dict = {}
    for l, u in zip(ascii_lowercase, ascii_uppercase):
        swap_dict[l] = u
        swap_dict[u] = l
        
    return ''.join([swap_dict[char] if char in swap_dict else char for char in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
