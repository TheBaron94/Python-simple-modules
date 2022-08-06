# LAB 4.17
# Adam Schmidt
# A mad lib program.

mad = input().split()

while mad[0] != 'quit':
    print('Eating {number} {thing} a day keeps the doctor away.'.format(
        number=mad[1], thing=mad[0]
    ))
    mad = input().split()
