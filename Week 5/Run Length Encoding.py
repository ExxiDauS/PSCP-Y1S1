"""Run Length Encoding"""

def encode(msg):
    'encode msg'
    encode_msg = ""
    count = 0
    count_msg = 0
    for char in msg:
        if char == msg[count_msg]:
            count += 1
        else:
            encode_msg += str(count) + msg[count_msg]
            count_msg += count
            count = 1
    encode_msg += str(count) + msg[count_msg]
    print(encode_msg)

encode(str(input()))
