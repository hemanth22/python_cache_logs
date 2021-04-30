with open('abc.log','r') as f:
    for line in f:
        line=line.strip()
        tim,msg,info=line.split()
        if 'error' in msg or 'warning' in msg:
            print(line)
