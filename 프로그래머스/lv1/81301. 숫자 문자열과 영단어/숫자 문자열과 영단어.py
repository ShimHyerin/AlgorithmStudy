def solution(s):
    d = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    tmp = ''
    anw = ''
    for i in s:
        if i.isdigit():
            anw += i
        else:
            tmp += i
            if tmp in d:
                anw += str(d.index(tmp))
                tmp = ''
    # if tmp:
    #     anw += d.index(tmp)
    return int(anw)