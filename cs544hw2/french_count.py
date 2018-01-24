import sys
from fst import FST
from fsmutils import composewords,trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.add_state('hundreds')
    f.add_state('tens')
    f.add_state('11to19')
    f.add_state('70')
    f.add_state('80')
    f.add_state('90')
    f.add_state('units')
    f.add_state('zeros')
    f.add_state('099')
    f.add_state('010')
    f.initial_state = 'start'

    for ii in xrange(10):
        if ii > 1:
            f.add_arc('start', 'hundreds', [str(ii)], [kFRENCH_TRANS[ii]+" "+kFRENCH_TRANS[100]])
            f.add_arc('tens', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('80', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('zeros', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('010', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            if ii<7:
                f.add_arc('hundreds', 'tens', [str(ii)], [kFRENCH_TRANS[ii*10]])
                f.add_arc('099', 'tens', [str(ii)], [kFRENCH_TRANS[ii*10]])
                f.add_arc('11to19', 'units', [str(ii)], [kFRENCH_TRANS[10+ii]])
                f.add_arc('90', 'units', [str(ii)], [kFRENCH_TRANS[10+ii]])
                f.add_arc('70', 'units', [str(ii)], [kFRENCH_TRANS[10+ii]])
            else:
                if ii == 7:
                    f.add_arc('hundreds', '70', [str(ii)], [kFRENCH_TRANS[60]])
                    f.add_arc('099', '70', [str(ii)], [kFRENCH_TRANS[60]])
                elif ii == 9:
                    f.add_arc('hundreds', '90', [str(ii)], [kFRENCH_TRANS[ii/2]+" "+kFRENCH_TRANS[20]])
                    f.add_arc('099', '90', [str(ii)], [kFRENCH_TRANS[ii/2]+" "+kFRENCH_TRANS[20]])
                else:
                    f.add_arc('hundreds', '80', [str(ii)], [kFRENCH_TRANS[ii / 2] + " " + kFRENCH_TRANS[20]])
                    f.add_arc('099', '80', [str(ii)], [kFRENCH_TRANS[ii / 2] + " " + kFRENCH_TRANS[20]])
                f.add_arc('11to19', 'units', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[ii]])
                f.add_arc('90', 'units', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[ii]])
                f.add_arc('70', 'units', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[ii]])
        elif ii == 0:
            f.add_arc('start', '099', [str(ii)], [])
            f.add_arc('099', '010', [str(ii)], [])
            f.add_arc('010', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('hundreds', 'zeros', [str(ii)], [])
            f.add_arc('tens', 'units', [str(ii)], [])
            f.add_arc('70', 'units', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('80', 'units', [str(ii)], [])
            f.add_arc('90', 'units', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('11to19', 'units', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('zeros', 'units', [str(ii)], [])
        else:
            f.add_arc('start', 'hundreds', [str(ii)], [kFRENCH_TRANS[100]])
            f.add_arc('tens', 'units', [str(ii)], [kFRENCH_TRANS[ii+1]])
            f.add_arc('hundreds', '11to19', [str(ii)], [])
            f.add_arc('099', '11to19', [str(ii)], [])
            f.add_arc('11to19', 'units', [str(ii)], [kFRENCH_TRANS[ii+10]])
            f.add_arc('tens', 'units', [str(ii)], [kFRENCH_AND+" "+kFRENCH_TRANS[ii]])
            f.add_arc('70', 'units', [str(ii)], [kFRENCH_AND+" "+kFRENCH_TRANS[ii+10]])
            f.add_arc('80', 'units', [str(ii)], [ kFRENCH_TRANS[ii]])
            f.add_arc('90', 'units', [str(ii)], [kFRENCH_TRANS[ii+10]])
            f.add_arc('zeros', 'units', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('010', 'units', [str(ii)], [kFRENCH_TRANS[ii]])

    f.set_final('units')
    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
