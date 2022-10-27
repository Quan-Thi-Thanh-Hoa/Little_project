import math
#Nhập input
 
n = 6
x = []
x = toa_do = [0,0,0,1,2,1]
#tương ứng [Ax, Ay, Bx, By, Cx, Cy]
 
a1 = math.sqrt(((x[2] - x[0])**2 + (x[3] - x[1])**2)) #a1 là độ dài cạnh AB
a2 = math.sqrt(((x[4] - x[0])**2 + (x[5] - x[1])**2)) #a2 là độ dài cạnh AC
a3 = math.sqrt(((x[4] - x[2])**2 + (x[5] - x[3])**2)) #a3 là độ dài cạnh BC
 
#a. Kiểm tra xem 3 điểm A, B, C có đủ điều kiện hợp thành tam giác ABC hay không
 
def kiemtra_tamgiac(input):
    if a1 + a2 < a3 and a1 + a3 < a2 and a2 + a3 < a1:
        return False
    else:
        return True

#b. Tính toán các cạnh và góc của tam giác ABC:
 
def goccanh_tamgiac(input):
 
    #Độ dài cạnh AB, AC, BC:
    a = round(a1,2)
    b = round(a2,2)
    c = round(a3,2)
    print(f'Độ dài cạnh AB: {a}')
    print(f'Độ dài cạnh AC: {b}')
    print(f'Độ dài cạnh BC: {c}')
 
    #Số đo các góc của tam giác ABC(cos => radian => degrees):
    cosA = (a**2 + b**2 - c**2) / (2*a*b)
    gocA = round(math.degrees(math.acos(cosA)),2)
    print(f'Goc A : {gocA}')
 
    cosB = (a**2 + c**2 - b**2) / (2*a*c)
    gocB = round(math.degrees(math.acos(cosB)),2)
    print(f'Goc B : {gocB}')
 
    cosC = (b**2 + c**2 - a**2) / (2*b*c)
    gocC = round(math.degrees(math.acos(cosC)),2)
    print(f'Goc C : {gocC}')

    return (a, b, c, gocA, gocB, gocC)
 
#Xác định lại biến cho các tham số trên để sử dụng cho các yêu cầu về sau:
cosA = (a1**2 + a2**2 - a3**2) / (2*a1*a2)
cosB = (a1**2 + a3**2 - a2**2) / (2*a1*a3)
cosC = (a2**2 + a3**2 - a1**2) / (2*a2*a3)

#Độ dài cạnh AB, AC, BC:
a = round(a1,2)
b = round(a2,2)
c = round(a3,2)
 
gocA = round(math.degrees(math.acos(cosA)),2)
gocB = round(math.degrees(math.acos(cosB)),2)
gocC = round(math.degrees(math.acos(cosC)),2)
 
#c. Xét xem tam giác ABC thuộc loại tam giác nào:
 
def xet_tamgiac(input):
 
    #Xét xem tam giác ABC là tam giác vuông, tam giác nhọn hay tam giác tù, tại đỉnh nào:
    if gocA == 90 and a1 == a2:
        print(f'ABC la tam giac vuong can tai dinh A : {gocA}')
    elif gocB == 90 and a1 == a3:
        print(f'ABC la tam giac vuong can tai dinh B : {gocB}')
    elif gocC == 90 and a2 == a3:
        print(f'ABC la tam giac vuong can tai dinh C : {gocC}')
 
    elif a1 == a2 and a2 == a3:
        print("ABC la tam gia deu")
 
    elif gocA == 60 and gocB == 60 and gocC == 60:
        print("ABC la tam gia deu")
   
    elif gocA > 90 and a1 == a2:
        print(f'ABC la tam giac tu va can tai dinh A : {gocA}')
    elif gocB > 90 and a1 == a3:
        print(f'ABC la tam giac tu va can tai dinh B : {gocB}')
    elif gocC > 90 and a2 == a3:
        print(f'ABC la tam giac tu va can tai dinh C : {gocC}')
 
    if gocA == 90 and a2 != a3:
        print(f'ABC la tam giac vuong tai dinh A : {gocA}')
    elif gocB == 90 and a1 != a3:
        print(f'ABC la tam giac vuong tai dinh B : {gocB}')
    elif gocC == 90 and a2 != a3:
        print(f'ABC la tam giac vuong tai dinh C : {gocC}')
 
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("ABC la tam giac can")
 
    elif gocA > 90 and a1 != a2:
        print(f'ABC la tam giac tu tai dinh A : {gocA}')
    elif gocB > 90 and a1 != a3:
        print(f'ABC la tam giac tu tai dinh B : {gocB}')
    elif gocC > 90 and a2 != a3:
        print(f'ABC la tam giac tu tai dinh C : {gocC}')
   
    else:
        print("ABC la tam giac binh thuong")
 
#d. Tinh dien tich tam giac ABC:
area = round((0.5 * a1 * a2 * math.sin(gocA)), 2)
def dientich_tamgiac(input):
    return round(area, 2)
 
#e. Tính độ dài của các đường cao của tam giác ABC:
 
# nửa chu vi tam giác ABC:
p = (a1 + a2 + a3) / 2
 
dcA = round(2*(math.sqrt(p * (p - a1) * (p - a2) * (p - a3)))/a3, 2)
dcB = round(2*(math.sqrt(p * (p - a1) * (p - a2) * (p - a3)))/a2, 2)
dcC = round(2*(math.sqrt(p * (p - a1) * (p - a2) * (p - a3)))/a1, 2)
 
def duongcao_tamgiac(input):
    list = ["dcA", "dcB", "dcC"]
    for h in list :
        if h == True :
            print("\"h\" la duong cao cua tam giac ABC");
    
    return (dcA, dcB, dcC)
 
#f. Tính độ dài từ các đỉnh A, B, C đến trọng tâm tam giác ABC:

mA = round(math.sqrt(((a2**2 + a3**2)/2) - (a1**2)/4), 2)
mB = round(math.sqrt(((a1**2 + a3**2)/2) - (a2**2)/4), 2)
mC = round(math.sqrt(((a1**2 + a2**2)/2) - (a3**2)/4), 2)

def trungtuyen_tamgiac(input):
    list = ["ttA", "ttB", "ttC"]
    for t in list :
        if t == True :
            print("t la trung tuyen tam giac ABC");
        
    return (mA, mB, mC)

# g. Tọa độ trọng tâm và trực tâm của tam giác ABC

trongtam_x = round((x[0] + x[2] + x[4]) /3, 2)
trongtam_y = round((x[1] + x[3] + x[5]) /3, 2)

def trongtam_tamgiac(input):
    list = ["trongtam_x", "trongtam_y", "tructam_x", "tructam_y"]
    for T in list :
        if T == True :
            print("T la trong tam tam giac ABC");

    return [trongtam_x, trongtam_y]

#Tọa độ BC(a1;a2); AC(a3;a4); AH(xH - x[0]; yH - x[1]); BH(xH - x[2]; yH - x[3])
a1 = x[4] - x[2]
a2 = x[5] - x[3]
a3 = x[4] - x[0]
a4 = x[5] - x[4]

#Tam giác ABC có trực tâm H
#Vecto(AH).vecto(BC) = 0
#Vecto(BH).vecto(AC) = 0

#Tính các định thức
D = a1*a4 - a2*a3
Dx = a4*(a1*x[0] + a2*x[1]) - a2*(a3*x[2] + a4*x[3])
Dy = a1*(a3*x[2] + a4*x[3]) - a3*(a1*x[0] + a2*x[1])

#Công thức Cramer
xH = Dx/D
yH = Dy/D

def tructam_tamgiac(input):
    return [xH, yH]

# h.Trả về tất cả các kết quả ở trên:
def giaima_tamgiac(input):
    if kiemtra_tamgiac(input):
        print ("A, B, C hop thanh mot tam giac")
    
    else:
        from sys import exit
        exit("A, B, C khong hop thanh mot tam giac")

print ("1. So do co ban cua tam giac:")
print ("Chieu dai canh AB:", a)
print ("Chieu dai canh AC:", b)
print ("Chieu dai canh BC:", c)
print ("Goc A:", gocA)
print ("Goc B:", gocB)
print ("Goc C:", gocC)
xet_tamgiac (input) 
print ("2. Dien tich cua tam giac ABC:", area)
print ("3. So do nang cao tam giac ABC:")
print ("Do dai duong cao tu dinh A:", dcA)
print ("Do dai duong cao tu dinh B:", dcB)
print ("Do dai duong cao tu dinh C:", dcC)
print ("Khoang cach den trong tam tu dinh A:", mA)
print ("Khoang cach den trong tam tu dinh B:", mB)
print ("Khoang cach den trong tam tu dinh C:", mC)
print("4. Toa do mot so diem dac biet cua tam giac ABC:")
print("Toa do trong tam:", trongtam_tamgiac(input))
print("Toa do truc tam:", tructam_tamgiac(input))

giaima_tamgiac(input)

