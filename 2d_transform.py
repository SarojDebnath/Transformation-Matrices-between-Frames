import numpy as np
src=[]
dst=[]
for i in range(0,3):
    src.append([float(value) for value in input(f'Enter source point{i+1} separated by a space=\t').split(' ')])
    dst.append([float(v) for v in input(f'Enter destination point{i+1} separated by a space=\t').split(' ')])
#src=[[-1,-1],[0,0],[0,1]]
#dst=[[0,0],[1,1],[1,2]]
a = np.array([[src[0][0],src[0][1],1],[src[1][0],src[1][1],1],[src[2][0],src[2][1],1]])
b = np.array([dst[0][0],dst[1][0],dst[2][0]])
x = np.linalg.solve(a, b)
x=np.asmatrix(x)

c = a
d = np.array([dst[0][1],dst[1][1],dst[2][1]])
y = np.linalg.solve(c, d)
y=np.asmatrix(y)

hom_row=np.asmatrix([0.,0.,1.])

k=np.concatenate((x,y,hom_row),0)
print('Transformation_Matrix:\n',k)
count=0
while (count<3):
    p1=input('Enter a Source point:\t')
    p = [float(value) for value in p1.split(' ')]
    p.append(1)
    dst_p=np.matmul(k,p)
    dst_p=dst_p.tolist()
    dst_p=(dst_p[0])[:-1]
    print(dst_p)
    del p1
    del p
    count+=1