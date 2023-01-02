def Hanoi(disks, source, aux, output):
    if disks == 1:
        print('Move disk 1 from rod {} to rod {}.'.format(source, output))
        return
 
    Hanoi(disks - 1, source, output, aux)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, output))
    Hanoi(disks - 1, aux, source, output)
 
disks = int(input('Enter number of disks: '))
Hanoi(disks, 'A', 'B', 'C')