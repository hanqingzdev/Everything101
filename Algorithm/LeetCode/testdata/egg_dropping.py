class EggDroppingTestData():
    @staticmethod
    def _generate(inputs):
        return [ (n, k, EggDroppingTestData.solution(n, k)) for (n, k) in inputs ]

    @staticmethod
    def basic():
        return EggDroppingTestData._generate([(1, 5), (2, 6), (5, 10)])

    @staticmethod
    def big():
        return EggDroppingTestData._generate([(5, 100), (6, 1000), (10, 2000)])

    @staticmethod
    def solution(N, K):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, N+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= K: break
            return ans

        lo, hi = 1, K
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < K:
                lo = mi + 1
            else:
                hi = mi
        return lo
