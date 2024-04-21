# Enter your code here. Read input from STDIN. Print output to STDOUT
r_d, r_m, r_y = list(map(int, input().split()))
e_d, e_m, e_y = list(map(int, input().split()))

if r_y < e_y:
    fine = 0
elif r_y > e_y:
    fine = 10000
else:
    if r_m < e_m:
        fine = 0
    elif r_m > e_m:
        fine = 500 * (r_m - e_m)
    else:
        if r_d <= e_d:
            fine = 0
        else:
            fine = 15 * (r_d - e_d)

print(fine)
