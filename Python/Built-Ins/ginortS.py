# First Approach
from string import ascii_lowercase, ascii_uppercase


order = ascii_lowercase + ascii_uppercase + '13579' + '02468'
print(''.join(sorted(input(), key=order.index)))

# Second Approach

print(
    ''.join(
        sorted(
                input(), 
                key=lambda x: (
                    x.isdigit() and int(x) % 2 == 0,
                    x.isdigit() and int(x) % 2 == 1,
                    x.isupper(),
                    x.islower(),
                    x
                )
        )
    )
)
