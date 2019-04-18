import sys
import itertools
class TSP:
    def BF(self, matrix):
        row_count = len(matrix)
        if row_count == 0:
            return 0
        cities = [i for i in range(1, row_count)]
        all_permutations = itertools.permutations(cities, row_count-1)
        m = float('inf')
        for r in all_permutations:
            temp_max = 0
            temp_max += matrix[0][r[0]]
            for i in range(len(r)):
                if i < len(r) - 1:
                    temp_max += matrix[r[i]][r[i+1]]
                elif i == len(r) - 1:
                    temp_max += matrix[r[i]][0]
                else:
                    print('ll')
            if temp_max < m:
                m = temp_max
        return m
    def BF_rec(self, matrix):
        row_count = len(matrix)
        if row_count == 0:
            return 0
        self.store = {}
        cities = [i for i in range(1, row_count)]
        return self._BF_rec(0, 0, cities)
    def _BF_rec(self, S, E, path):
        if len(path) == 1:
            return matrix[S][path[0]] + matrix[path[0]][E]
        temp = []
        for city in path:
            path_next = path[:]
            path_next.remove(city)
            temp.append(self._BF_rec(city, E, path_next) + matrix[S][city])
        return min(temp)
    def DP(self, matrix):
        row_count = len(matrix)
        if row_count == 0:
            return 0
        self.store = {}
        cities = [i for i in range(1, row_count)]
        return self._DP(0, 0, cities)
    def _DP(self, S, E, path):
        if len(path) == 1:
            return matrix[S][path[0]] + matrix[path[0]][E]
        temp = []

        # worong 错在没加入起点，比如 1 -> [2, 3, 4] 就不等于 5 -> [2, 3, 4]， 所以不能仅用path生成key
        # if self.store.get(tuple(path)):
        #     print('get from store: ' + str(tuple(path)))
        #     return self.store[tuple(path)]

        key = [S]
        key.extend(path)
        if self.store.get(tuple(key)):
            print('get from store: ' + str(tuple(key)))
            return self.store[tuple(key)]
        
        for city in path:
            path_next = path[:]
            path_next.remove(city)
            temp.append(self._DP(city, E, path_next) + matrix[S][city])
        res = min(temp)
        self.store[tuple(key)] = res
        return res
if __name__ == '__main__':
    matrix = []
    matrix.append(list(map(float, input().strip().split())))
    row_count = len(matrix[0])
    iternum = row_count
    while iternum > 1:
        iternum -= 1
        matrix.append(list(map(float, input().strip().split())))

    tsp = TSP()
    m = tsp.BF(matrix)
    print('BF:', str(m))

    m = tsp.BF_rec(matrix)
    print('BF_rec:', str(m))

    m = tsp.DP(matrix)
    print('DP:', str(m))