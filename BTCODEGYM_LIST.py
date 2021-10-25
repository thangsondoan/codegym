# Khởi  tạo một list chứa các số cho trước. Tìm hai số lớn nhất của list vừa tạo được

listNumber = [54, 555, 32, 3, 4, 899, 4, 342, 3, 1]
if len(listNumber) >= 2:
    listNumber.sort()
    print(listNumber)
    print("Hai so lon nhat la: ", listNumber[-1], listNumber[-2])
else:
    print("List chua it hon 2 phan tu.")