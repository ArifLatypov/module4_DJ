 #АЛГОРИТМ O(N^2) или O(N * M) :
 #(M - количество уникальных значений)
 #(N - общие количества значений)

#def strcounter(s):
    # for sym in set(s):
    #     count = 0
    #     for sub_sym in s:
    #         if sym == sub_sym:
    #             count += 1
    #     print(sym, count)
#strcounter("abcabc")
  
 # АЛГОРИТМ O(N)
def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    
    for sym, count in syms_counter.items():
        print(sym, count)
    
strcounter("abckfaa")

