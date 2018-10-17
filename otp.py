#============== Shift Right ================= #

def right(s,n1):
    '''
    Shifts the characters to the right

    s = string being manipulated by the puzzle
    n1 = how many positions the function shifts the string

    Return Value: the new string after the shift

    '''
        
    return s[-n1:] + s[:-n1]

#============== Shift Left ================= #

def left(s,n1):
    '''
    Shifts the characters to the left

    s = string being manipulated by the puzzle
    n1 = how many positions the function shifts the string

    Return Value: the new string after the shift

    '''
    return s[n1:] + s[:n1]

#============== Rotate Function ================= #

def twist(s,n1,n2):
    '''
    Swaps the two positions of the characters.

    Parameters:
    s = string being manipulated by the puzzle.
    n1 = the first character input
    n2 = the second character input

    Return Value: the final rotated string


    '''


    twist_s = list(s)
    twist_s[n1], twist_s[n2] = twist_s[n2], twist_s[n1]
    
    return ''.join(twist_s)

#============== Main Function ================= #

def main():


    s = input("Enter string s: ")

    b = s

    z = 'A'

    while z != ['S']:
        i = input("Enter command: ")
        d = i.split(" ")
        cmdlist = [d]
        c = d[0]
        
        if c == 'R':
            n1 = int(d[1])
            R = right(s,n1)
            s = R
            print(R)

        elif c == 'L':
            n1 = int(d[1])
            L = left(s,n1)
            s = L
            print(L)

        elif c == 'S':
            if s == b:
                print("Puzzle Solved")
            else:
                print("Puzzle not Solved")
                
            break
        
        else:

            c, n1, n2 = i.split()
            n1 = int(d[1])
            n2 = int(d[2])
            
            T = twist(s,n1,n2)
            s = T
            print(T)
            

main()
        
#============== END ================= #
