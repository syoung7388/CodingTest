import sys
N = int(input())
tree = {}
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root): #루트 -> 왼쪽 -> 오른쪽
    if root != '.':
        print(root, end = "")
        preorder(tree[root][0]) #왼쪽
        preorder(tree[root][1]) #오른쪽 
        
def inorder(root): #왼쪽 -> 루트 -> 오른쪽
    if root != '.':
        inorder(tree[root][0])
        print(root, end = "")
        inorder(tree[root][1])
def postorder(root):
    if root != '.': # 왼쪽 -> 오른쪽 -> 루트
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")
preorder('A')
print()
inorder('A')
print()
postorder('A')
