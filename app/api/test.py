import ctypes

# the .so file is created with
# gcc proto.c -o proto.so -lpigpio -pthread -shared 

file = "/home/klithik/protesis/app/api/proto.so"
funciones = ctypes.CDLL(file)

arr1 = (ctypes.c_int * 6)(1,2,3,4,5,6)
arr2 = (ctypes.c_int * 6)(7,8,9,10,11,12)
print(funciones.move(arr1,arr2))
