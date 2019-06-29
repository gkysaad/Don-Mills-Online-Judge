rabbits = int(input())
groups = int(input())
if rabbits/groups >= 1:
    print(min(rabbits%groups, groups - rabbits%groups))
else:
    print(groups- rabbits)
