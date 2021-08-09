def count_substring(string, sub_string):
    count = 0
    stard_ind = 0
    while True:
        ind = string.find(sub_string, stard_ind)
        if ind == -1:
            break
        else:
            stard_ind = ind + 1
            count += 1
            
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
