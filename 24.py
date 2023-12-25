lines = []
with open("24_data.txt") as f:
    data = f.read().strip().split("\n")
    for l in data:
        spl = l.split("@")
        px, py, pz = [int(n) for n in spl[0].split(",")]
        vx, vy, vz = [int(n) for n in spl[1].split(",")]
        lines.append((px, py, pz, vx, vy, vz))

square = (200000000000000, 400000000000000)
#square = (7, 27)
answer = 0

while len(lines) > 0:
    px, py, _, vx, vy, _ = lines.pop(0)

    _angle = vy / vx
    _constant = py - (_angle * px)

    for intersect in lines:
        ix, iy, _, ivx, ivy, _ = intersect
        i_angle = ivy / ivx
        if i_angle == _angle:
            continue
        i_constant = iy - (i_angle * ix)

        x = (_constant - i_constant) / (i_angle - _angle)
        y = _constant + _angle * x

        _t = (x - ix) / ivx > 0 and (x - px) / vx > 0
    
        if _t and square[0] <= x <= square[1] and square[0] <= y <= square[1]:
            answer += 1

print("Answer 1:", answer)
