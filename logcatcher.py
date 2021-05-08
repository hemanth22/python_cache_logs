with open('abc.log','r') as f:
    for line in f:
        line=line.strip()
        try:
            new=line.split()
            if 'error' in new[1]:
                print(line)
        except Exception as e:
            print(e)

