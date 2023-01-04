import numpy as np
src=[]
dst=[]
for i in range(0,4):
    src.append([float(value) for value in input(f'Enter source point{i+1} separated by a space').split(' ')])
    dst.append([float(v) for v in input(f'Enter destination point{i+1} separated by a space').split(' ')])
a = np.array([[src[0][0],src[0][1],src[0][2],1],[src[1][0],src[1][1],src[1][2],1],[src[2][0],src[2][1],src[2][2],1],[src[3][0],src[3][1],src[3][2],1]])
b = np.array([dst[0][0],dst[1][0],dst[2][0],dst[3][0]])
x = np.linalg.solve(a, b)
x=np.asmatrix(x)

c = a
d = np.array([dst[0][1],dst[1][1],dst[2][1],dst[3][1]])
y = np.linalg.solve(c, d)
y=np.asmatrix(y)

e=a
f = np.array([dst[0][2],dst[1][2],dst[2][2],dst[3][2]])
z = np.linalg.solve(e, f)
z=np.asmatrix(z)


hom_row=np.asmatrix([0.,0.,0.,1.])

k=np.concatenate((x,y,z,hom_row),0)
print('Transformation_Matrix:\n',k)
count=0
while (count<3):
    p1=input('Enter a Source point')
    p = [float(value) for value in p1.split(' ')]
    p.append(1)
    dst_p=np.matmul(k,p)
    dst_p=dst_p.tolist()
    dst_p=(dst_p[0])[:-1]
    print(dst_p)
    del p1
    del p
    count+=1