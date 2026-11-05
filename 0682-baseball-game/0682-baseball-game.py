class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        sum = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                sum += record[-2] + record[-1]
                record.append(record[-2] + record[-1])
            elif operations[i] == "D":
                sum += 2 * record[-1]
                record.append(2 * record[-1])
            elif operations[i] == "C":
                sum -= record.pop()
            else: 
                record.append(int(operations[i]))
                sum += int(operations[i])
        return sum
        