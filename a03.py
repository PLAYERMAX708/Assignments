## IMPORTS GO HERE
## END OF IMPORTS

#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def good_enough (guess, num):
    if abs(guess*guess-num) < 0.00001:
        return True
    else:
        return False

def abs(num):
    if num >= 0:
        return num
    else:
        return -num

def sqrt (num, guess=1):
    if good_enough(guess, num):
        return guess
    else:
        better_guess = improve_guess(guess, num)
        return sqrt(num, better_guess)

#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average (num1, num2):
    return (num1+num2)/2
#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess (guess, num):
    # num = num * 1.0            # this is not required as the updated python version has handled this inconvenience -- ( * ) ___ ( * ) -- 
    return average(guess, num/guess)    # asked a comment from sir about the zerodivisionerror
#### End OF MARKER




if __name__ == '__main__':
    print (sqrt(36))
