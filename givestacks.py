import math

jtype = input("Type: cutdown | or |  default? ") # jobtype - (125 stacks) or (250 stacks)
itns = input("what is the total number of sheets? ") # total number sheets
tns = int(itns)
itln = input("what is the total number of labels? ") # total label number
tln = int(itln)

stacksize = 0

def givestacks(stacksize):
    sumofjtype = tns/stacksize
    trunc_sum = math.trunc(sumofjtype)
    subfromtotal = trunc_sum * stacksize
	
    if tln > 10: # total labels per sheet
        leftovercheck = stacksize - 15
    else:
        leftovercheck = stacksize - 10

    leftover = tns - subfromtotal
	
    if leftover < leftovercheck:
        print(str(trunc_sum) + ' stacks of ' + str(stacksize) + ' with ' + str(leftover) + ' as leftover.')
    else:
        new_tsum = trunc_sum + 1
        print(str(new_tsum) + ' stacks of ' + str(stacksize))

# print: {trunc_sum} stacks of {jtype(stacksize)} with a stack of {leftover}

if jtype == "default":
    stacksize = 250;
    print('250 Stacks for ' + str(tns))
    print('')
    givestacks(250)
elif jtype == "cutdown":
    stacksize = 125;
    print('125 Stacks for ' + str(tns))
    print('')
    givestacks(125)
else: 
    print('You must write |cutdown| or |default| for Type')

# {tns}1234 cd
# 1234 % 125{cd}
# sumofjtype = 9.872
# trunc_sum = math.trunc(sumofjtype)
# trunc_sum = 9
# trunc_sum{9} * cd{125}
# subfromtotal = 1,125
# tns - subfromtotal =
# 109
# 109 = leftover
# but check if leftover < 10 of jtype{cd(125)}
# 125 > 119
# so do not add 1 to trunc_sum
# print: {trunc_sum} stacks of {jtype} with a stack of {leftover}
####
# {tns}1234 def
# 1234 % 250{cd}
# sumofjtype = 4.396
# trunc_sum = math.trunc(sumofjtype)
# trunc_sum = 4
# trunc_sum{4} * def{250}
# subfromtotal = 1,000
# tns - subfromtotal = 234 
# 234 = leftover
# but check if leftover < 10 of jtype{def(250)}
# 250 > 244
# so do not add 1 to trunc_sum
# print: {trunc_sum} stacks of {jtype} with a stack of {leftover}

# total number % jtype
#######################

    ##  use math.trunc() to
    # take everything before decimal point 
    # e.g. 5.29 = 5
    # then find .29 
    # by doing mathTrun x jtype = precalc
    # subtract total from precalc = addtoTotal
    # formula is right if precalc + addtoTotal == tns
    # print(str(precalc) + ' stacks, with ' + addtoTotal)
    #
    # if addtoTotal is < 20 jtype just make it another stack 
    # add 1 to precalc
    # & print(str(precalc) + ' stacks)
