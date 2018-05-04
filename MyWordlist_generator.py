def word_gen(start= 3,end= 3, elements = 1):
    """
    Hud Seidu Daannaa Wordlist gen
    MSC InfoSec, CEH"
    
    README
    #for start&end
    #e.g. start= 3,end= 3
    #means first words to last words should be 3 characters
    
    #for elements
    1 is asci
    2 is numbers
    3 is asci&numbers
    """
    import itertools
    #types of elements
    if elements ==1: elements= 'abcdefghijklmnopqrstuvwxyx'
    if elements ==2: elements= '0123456789'
    if elements== 3: elements= 'abcdefghijklmnopqrstuvwxyx0123456789'
    else: pass
    wl = []
    for i in range(start,end+1):
        for xs in itertools.product(elements, repeat=i):
            wl.append(''.join(xs))
    return wl
