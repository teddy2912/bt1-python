import pandas as pd
# bai 1
 
# def docFile():
#     file = open('input', encoding='utf-8')
#     for line in file:
#         print(line.strip())
#     file.close
# docFile()

with open('input') as f:
    numbers = f.read().split()
soChan = 0
soLe = 0

for num in numbers:
    if int(num) % 2 == 0:
        soChan += 1
    else:
        soLe += 1 

print(f"Số lượng số chẵn là: {soChan}")
print(f"Số lượng số lẻ là: {soLe}")

# tim so luong so nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

so_nguyen_to = 0

for num in numbers:
    if is_prime(int(num)):
        so_nguyen_to += 1

print(f"Số lượng số nguyên tố là: {so_nguyen_to}")

# đếm số xuất hiện nhiều nhất
number_count = {}
max_count = 0
most_common = None

for num in numbers:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1

for num, count in number_count.items():
    if count > max_count:
        max_count = count
        most_common = num

print(f"Số xuất hiện nhiều nhất là: {most_common}, xuất hiện {max_count} lần")

# Bai 2 

# def dtb(diemToan, diemLy, diemHoa):
#     return(diemToan + diemLy + diemHoa) / 3

docFile = pd.read_excel('input.xlsx')

def sapXep(file):
    f = file
    f = f.iloc[10:62, 1:8]
    f = f.rename(columns = {f.columns[0]: 'id', f.columns[1]: 'ho', f.columns[2]: 'ten', f.columns[3]: 'ngay sinh', f.columns[4]: 'toan', f.columns[5]: 'ly', f.columns[6]: 'hoa'})
    f = f.sort_values(by = ['ten']) 
    print(f)
sapXep(docFile)

def thongKe(file):
    f = file
    f = f.iloc[10:62, 1:8]
    f = f.rename(columns={f.columns[0]: 'id', f.columns[1]: 'ho', f.columns[2]: 'ten', f.columns[3]: 'ngay sinh', f.columns[4]: 'toan', f.columns[5]: 'ly', f.columns[6]: 'hoa'})
    f['diem trung binh'] = (f['toan'] + f['ly'] + f['hoa']) / 3
    f['xep loai'] = f['diem trung binh'].apply(lambda x: "gioi" if x >= 8 else "kha" if x >= 6.5 else "trung binh")
 
    gioi = 0
    kha = 0
    trungBinh = 0

    for index in f.index:
        if f['diem trung binh'][index] >= 8:
            gioi += 1
        elif f['diem trung binh'][index] >= 6.5:
            kha += 1
        else:
            trungBinh += 1
    newF = pd.DataFrame({
        'Gioi': [gioi],
        'Kha': [kha],
        'Trung binh': [trungBinh]
    })
    print(f"Số học sinh giỏi: {gioi}")
    print(f"Số học sinh khá: {kha}")
    print(f"Số học sinh trung bình: {trungBinh}")

thongKe(docFile)