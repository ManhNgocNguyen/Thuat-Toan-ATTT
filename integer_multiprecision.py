import math


def numb_to_arr(a, p, w):
    array = []
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    while t >= 1:
        arr = a // pow(2, w * (t - 1))
        a = a % pow(2, w * (t - 1))
        array.append(arr)
        if t == 1:
            return array
        t -= 1
        
        
  def convert_uv_to_u_v(uv):
        bin_uv = str(bin(uv)[2:])
        if len(bin_uv) < 16:
            bin_uv = "0" * (16 - len(bin_uv)) + bin_uv # Trường hợp không đủ 16 bit thì chèn thêm các bit 0 vào trước
        u = int(bin_uv[:8], 2)
        v = int(bin_uv[8:], 2)
        return u, v
      
      
def multiple(p, a, b, w):
    a = numb_to_arr(a, p, w)[::-1]
    b = numb_to_arr(b, p, w)[::-1]
    m = math.ceil(math.log2(p))
    t = math.ceil(m / w)
    c = [0] * 2 * t #Khởi tạo mảng bằng 2 lần t vì tí còn add 2w bit vào mảng
    for i in range(t):
        u = 0
        for j in range(t):
            uv = c[i+j] + a[i] * b[j] + u
            u, v = convert_uv_to_u_v(uv)
            c[i+j] = v
        c[i+t] = u
    return c[::-1]
