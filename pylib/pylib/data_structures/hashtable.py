mods: list[int] = [1000000007, 2117566807]
bases: list[int] = [1572872831, 1971536491]


class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.forwardHashTable: list[int] = []
        self.backwardHashTable: list[int] = []
        self.power: list[int] = []
        self.power = [0] * self.size
        self.power[0] = 1

        for i in range(1, self.size):
            self.power[i] = (self.power[i - 1] * bases[0]) % mods[0]

    def makeForwardHashTable(self, string: str) -> None:
        sz = len(string)
        self.forwardHashTable = [0] * sz
        for i in range(sz):
            current = ord(string[i]) - ord(" ")

            if i != 0:
                self.forwardHashTable[i] = (
                    (self.forwardHashTable[i - 1] * bases[0]) % mods[0] + current
                ) % mods[0]

            else:
                self.forwardHashTable[i] = current

    def makeBackwardHashTable(self, string: str) -> None:
        sz = len(string)
        self.backwardHashTable = [0] * sz
        for i in range(sz - 1, 0, -1):
            current = ord(string[i]) - ord(" ")

            if i != sz - 1:
                self.backwardHashTable[i] = (
                    (self.backwardHashTable[i - 1] * bases[0]) % mods[0] + current
                ) % mods[0]

            else:
                self.backwardHashTable[i] = current

    def getForwardHashingQuery(self, left: int, right: int) -> int:
        if left == 0:
            return self.forwardHashTable[right] % mods[0]

        else:
            return self.MOD(
                self.forwardHashTable[right]
                - (
                    (self.forwardHashTable[left - 1] * self.power[right - left + 1])
                    % mods[0]
                )
            )

    def getBackwardHashingQuery(self, left: int, right: int | None = None) -> int:
        if right is None:
            return self.forwardHashTable[left]

        else:
            return self.MOD(
                self.backwardHashTable[left]
                - (self.backwardHashTable[right + 1] * self.power[right - left + 1])
                % mods[0]
            )

    def MOD(self, x: int) -> int:
        return (x + mods[0]) % mods[0]
