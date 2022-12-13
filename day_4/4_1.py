answer = 0

with open("4_test.txt") as f:
    for line in f:
        print(line.strip())
        small, big = sorted(line.strip().split(','))
        print([small, big])
        
        sa, sb = [ int(x) for x in small.split('-')]
        ba, bb = [ int(x) for x in big.split('-')]

        print(sa == ba and sb <= bb or sa <= ba and sb >= bb)

        if sa == ba and sb <= bb:
            answer += 1
        elif sa <= ba and sb >= bb:
            answer += 1

        break

        if answer > 10:
            break

print(answer)