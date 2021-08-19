from string import ascii_letters
from string import digits

def fun(s):
    l = s.split('@')
    if len(l) != 2:
        return False
    username = l[0]
    ll = l[1].split('.')
    if len(ll) != 2:
        return False
    website = ll[0]
    extension = ll[1]
    del l, ll
    if not username or not extension or not website:
        return False
    if len(extension) > 3:
        return False
    if (set(extension) - set(ascii_letters)) or \
        (set(website) - set(ascii_letters + digits)) or \
        (set(username) - set(ascii_letters + digits + '_-')):
        return False
    return True
    
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
