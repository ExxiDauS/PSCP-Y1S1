"""Ejudge"""
def main():
    """Solar System"""
    text = input()+' '
    temp, hot, cold, left_star, right_star = temp_maker(text, ''), '', '', None, None
    buffer, n_star, previous, previous_star, sun_pos = '', 0, -1, '', 0
    for i in temp:
        if i == ' ':
            n_star += 1
            current = text[previous+1:int(buffer)]
            if left_star is None:
                left_star = current + ' '
            if current == 'Sun':
                hot += previous_star + ' '
                sun_pos = n_star
            if previous_star == 'Sun':
                hot += current
            previous, previous_star = int(buffer), current
            buffer = ''
        elif i.isnumeric():
            buffer += str(i)
    if right_star is None:
        right_star = previous_star
    if text.strip() != 'Sun':
        if abs(1 - sun_pos) > abs(n_star - sun_pos):
            cold = left_star
        elif abs(1 - sun_pos) == abs(n_star - sun_pos):
            cold = left_star + right_star
        else:
            cold = right_star
    print('Hot: %s\nCool: %s'% (hot.strip(), cold.strip()))
def temp_maker(text, temp):
    '''Generate Temp Data'''
    for i, j in enumerate(text):
        if i > 2 and text[i-3] + text[i-2] + text[i-1] + j == 'Sun ':
            temp += str(i) + ' '
        elif j == ' ' and  text[i-3] + text[i-2] + text[i-1] + j != 'Sun ':
            temp += str(i) + ' '
    return temp
main()
