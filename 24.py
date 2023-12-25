lines = []
with open("24_data.txt") as f:
    data = f.read().strip().split("\n")
    for l in data:
        spl = l.split("@")
        px, py, pz = [int(n) for n in spl[0].split(",")]
        vx, vy, vz = [int(n) for n in spl[1].split(",")]
        # print(l)
        lines.append((px, py, pz, vx, vy, vz))

# print(lines)

square = (200000000000000, 400000000000000)
# square = (7, 27)
answer = 0

while len(lines) > 0:
    px, py, pz, vx, vy, vz = lines.pop(0)

    _angle = vy / vx
    _constant = py - (_angle * px)

    # print('_angle', _angle, _constant)

    for intersect in lines:
        ix, iy, iz, ivx, ivy, ivz = intersect
        i_angle = ivy / ivx
        if i_angle == _angle:
            # print("do not cross, parallel")
            continue
        i_constant = iy - (i_angle * ix)
        # print("i", i_angle, i_constant)
        # print("ic", _angle, i_angle, vy, vx, _constant, i_constant)
        # print("c", (_constant - i_constant), (i_angle - _angle))
        x = (_constant - i_constant) / (i_angle - _angle)
        y = _constant + _angle * x

        _t = x + px > px if _angle < 0 else x + px < px
        _t2 = x + ix > ix if i_angle > 0 else x + ix < ix

        # print('cross', x, y, x < px, x < ix, px, ix)
        # print("ns", _t, _t2, _angle, i_angle)
        if _t and _t2 and square[0] <= x <= square[1] and square[0] <= y <= square[1]:
            # print('add')
            answer += 1
        # print(x, i_constant + i_angle * x)
        # break
    # break
        
wrong = 'wrong' if answer <= 13066 else ''
print("Answer 1:", answer, wrong)

# To Low: 13066

