import typing

class sets:
    def __init__(self, Set: typing.Union[list, set, tuple]) -> None:
        self.Set, self.n = Set, len(Set)
        self.Hash = {}

    def Power_Set(s, pos = 0):
        """Power Set
            ========
            Generates a power set of the given input sequence

            Parameters
            ----------
            pos (optional) (default - 0) : int - Starting position in the input sequence from which the elements shoukd be considered

            Returns
            -------
            power set : list[list[int]] - power set of considered elements
        """
        subs = []
        for i in range(pos, s.n):
            if s.Hash.get(i, None) is None: s.Hash[i] = [[s.Set[i]]]+[[s.Set[i]] + sub for sub in s.Power_Set(i+1)]
            subs.extend(s.Hash[i])
        return subs