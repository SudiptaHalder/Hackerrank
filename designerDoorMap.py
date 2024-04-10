# Enter your code here. Read input from STDIN. Print output to S
n, m = map(int,input().split())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m,'-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))