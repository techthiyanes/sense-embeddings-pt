import re

sense = 1
#i = 0
cont = 0
word = ''
with open('./dois-senses/ptbreu_s300_sg', 'r', encoding='latin1') as f: #utf-8
    with open('./dois-senses/ptbreu_s300_sg.sense_vectors', 'w', encoding='latin1') as fmulti:
        line = f.readline()
        fmulti.write("937567 300\n")
        #wikipt 398080
        #wikipt.sense_vectors 804160
        #wikipt.sense_vectors #2,#3,#4 406080
        #wikien 369328
        #ptbreu 933567
        #ptbr.sense_vectors 1539456
        #ptbr.sense_vectors #2,#3,#4 773728
        for line in f:
            elements = line.split(' ')
            if len(elements) == 2:
                #print("Line: {}".format(line.strip()))
                word = elements[0]
                sense = 1
            else:
                if sense > 1:
                    fmulti.write(word + '#' + str(sense) + ' ') #+ '|' + str(sense)
                    fmulti.write(line) # + '\n'
                    cont = cont + 1
                    print('cont: ', cont)
                sense = sense + 1


    f.close()
fmulti.close()

#python3 convertvectors.py
