def rule_90(row):
    if row in ["111", "101", "010", "000"]:
        return "0"
    if row in ["110", "100", "011", "001"]:
        return "1"
    return None

def sliding(line, n): # Found from http://stackoverflow.com/a/9475354
    return [line[i:i+n] for i in range(len(line) - (n - 1))]

def replace_strings(state):
    return state.replace("1", "x").replace("0", " ")

def simulate(state, simulations):
    for run in range(simulations):
        print(replace_strings(state))
        state = "".join(rule_90(row) for row in sliding('0' + state + '0', 3))

if __name__ == "__main__":
    for state in ["1101010", "00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"]:
        simulate(state, 25)
