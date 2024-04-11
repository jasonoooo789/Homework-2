liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

id2token = [
    "tokenA",
    "tokenB",
    "tokenC",
    "tokenD",
    "tokenE"
]

token2id = {
    "tokenA": 0,
    "tokenB": 1,
    "tokenC": 2,
    "tokenD": 3,
    "tokenE": 4
}

def getAmountOut(token0, token1, token0In):
    try:
        reserve0, reserve1 = liquidity[(token0, token1)]
    except:
        reserve1, reserve0 = liquidity[(token1, token0)]
    return (997*token0In*reserve1)/(1000*reserve0+997*token0In)

def search(token, amount, path, mark):
    if token == 1 and mark[1] == True:
        return path, amount
    optimalAmount = 0
    optimalPath = None
    for i in range(5):
        if not mark[i] and i != token:
            amountOut = getAmountOut(id2token[token], id2token[i], amount)
            mark[i] = True
            candidatePath, candidateAmount = search(i, amountOut, path+[i], mark)
            mark[i] = False
            if candidateAmount > optimalAmount:
                optimalAmount = candidateAmount
                optimalPath = candidatePath
    return optimalPath, optimalAmount

def convertPath(path):
    ret = "path: "
    for i in path[:-1]:
        ret += id2token[i] + "->"
    ret += id2token[path[-1]]
    return ret

def main():
    path, amount = search(1, 5, [1], [False for _ in range(5)])
    # previous = 5
    # for i in range(len(path)-1):
    #     previous = getAmountOut(id2token[path[i]], id2token[path[i+1]], previous)
    #     print(previous)
    path = convertPath(path)
    print(path)
    print(f"tokenB balance={amount}")

if __name__ == "__main__":
    main()