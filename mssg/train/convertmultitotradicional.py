import re

sense = 1
i = 0
cont = 0
word = ''
with open('./dois-senses/ptbreu_s300_sg', 'r', encoding='latin1') as f: #latin1
    with open('./dois-senses/multisense_s300_ptbreu_sg.txt', 'w', encoding='latin1') as fmulti:
        line = f.readline()
        fmulti.write("933567 300\n")
        #wikipt 398080
        #wikien 369328
        #ptbreu 933567
        for line in f:
            elements = line.split(' ')
            if len(elements) == 2:
                #print("Line: {}".format(line.strip()))
                word = elements[0]
                sense = 1
            else:
                if sense == 1:
                    fmulti.write(word + ' ') #+ '|' + str(sense)
                    fmulti.write(line) # + '\n'
                    sense = sense + 1
                    cont = cont + 1
                    print('cont: ', cont)
        i = i + 1
    f.close()
fmulti.close()

#python3 convertmultitotradicional.py
