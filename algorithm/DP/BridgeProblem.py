class BridgeProblem:
    def two_go_one_back(self, T):
        T.sort()
        l = len(T)
        if l == 0:
            return None
        elif l == 1:
            return T[0]
        elif l == 2:
            return T[1]
        elif l == 3:
            return T[0]+T[1]+T[2]
        store = [T[0], T[1], T[0]+T[1]+T[2]]
        i = 3
        while i < l:
            store.append(min(store[i-1]+T[0]+T[i], store[i-2]+T[i]+2*T[1]+T[0]))
            i += 1
        return store[l-1]
    def three_go_two_back(self, T):
        T.sort()
        l = len(T)
        if l <= 1:
            return None
        elif l == 2:
            return T[1]
        elif l == 3:
            return T[2]
        elif l == 4:
            return T[1] + T[2] + T[3]
        store = [T[0], T[1], T[2], T[1] + T[2] + T[3]]
        i = 4
        while i < l:
            store.append(min(store[i-1]+T[1]+T[i], store[i-2]+T[1]+T[i]+T[2]+T[2], store[i-3]+T[1]+T[i]+T[3]+T[2]+T[1]+T[3]))
            i += 1
        return store[l-1]
    def three_go_one_back(self, T):
        T.sort()
        # to be continued

if __name__ == '__main__':
    print('test two_go_one_back, please input Times T[n]:')
    persons = list(map(float, input().strip().split()))
    b = BridgeProblem()
    n = b.two_go_one_back(persons)
    print('two_go_one_back: ', str(n))
    # 答案未验证
    print('test three_go_two_back, please input Times T[n]:')
    persons = list(map(float, input().strip().split()))
    n = b.three_go_two_back(persons)
    print('three_go_two_back: ', str(n))