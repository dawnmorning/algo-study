import math

file = open("input/230702_BAEK_1475_방_번호.txt")
room_num = file.readline().strip()

char_arr = list(room_num)
cnt_arr = [0] * 9

for c in char_arr:
    if c == "6" or c == "9":
        cnt_arr[6] += 0.5
    else:
        cnt_arr[int(c)] += 1

ans = math.ceil(max(cnt_arr))

print(ans)