import re

answer = 0

with open("12_data.txt") as f:
    for line in f:
        parts = line.split(" ")
        groups = [int(n) for n in parts[1].split(",")]

        few_options = len(parts[0]) - (sum(groups) + len(groups) - 1)

        # Filter out everything that only has 1 possibility.
        if few_options <= 1 or sum(groups) == parts[0].count("#") + parts[0].count("?") or sum(groups) + len(groups) - 1 == len(parts[0]):
            answer += 1
            continue

        gm = re.findall(r"([\?|#]+)", parts[0])
        c = 1
        if len(groups) == len(gm):
            for i, n in enumerate(groups):
                if n < len(gm[i]):
                    c = c * (len(gm[i])/n)
                    # print("Amount:", len(gm[i])/n)
                # print(n, len(gm[i]))
            # print("Groups", gm)
            # print("C", c)
            answer += c
        else:
            print(line.strip("\n"))
            print(few_options, sum(groups) + len(groups) - 1, parts[0].count("#") + parts[0].count("?"))

            


        # hashes = []
        # bigest = 0
        # for n in groups:
        #     hashes.append("#" * n)
        #     if n > bigest:
        #         bigest = n

        # gm = re.search(r"([\?|#]+)", parts[0])
        # print(hashes)
        # print(len(gm.groups()))
        # if len(gm.groups()) < len(hashes):
        #     # Search for specific hash?
        #     for n in sorted(hashes, reverse=True):
        #         print(n)
        #         if re.search(n, parts[0]):
        #             print("Found", n)
        #             break

print("Asnwer 1:", answer)

# ?###???????? 3,2,1
# .###.##.#...
# .###.##..#..
# .###.##...#.
# .###.##....#
# .###..##.#..
# .###..##..#.
# .###..##...#
# .###...##.#.
# .###...##..#
# .###....##.#