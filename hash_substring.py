# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())
    
    datatype=input()
    if "I" in datatype:
        return input().rstrip(), input().rstrip()

    if "F" in datatype:
        filepath="tests/06"
        with open(filepath, "r") as f:
            return f.readline().rstrip(), f.readline().rstrip()

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    # return [0]
    b=13
    q=256
    p=len(pattern)
    t=len(text)
    pathash=0
    texthash=0
    h=1
    occurences=[]

    for i in range(p-1):
        h=(h*q)%b

    for j in range(p):
        pathash=(q*pathash+ord(pattern[j]))%b
        texthash=(q*texthash+ord(text[j]))%b

    for i in range(t-p+1):
        if pathash==texthash and text[i:i+p]==pattern:
            occurences.append(i)

        if i<t-p:
            texthash=(q*(texthash-ord(text[i])*h)+ord(text[i+p]))%b
            if texthash<0:
                texthash+=1

    return occurences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

