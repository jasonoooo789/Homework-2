# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
path: tokenB->tokenA->tokenD->tokenC->tokenB
| swap           | amountIn           | amountOut          |
|----------------|--------------------|--------------------|
| tokenB->tokenA | 5                  | 5.655321988655322  |
| tokenA->tokenD | 5.655321988655322  | 2.4587813170979333 |
| tokenD->tokenC | 2.4587813170979333 | 5.0889272933015155 |
| tokenC->tokenB | 5.0889272933015155 | 20.129888944077443 |
final reward: 20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
To ensure that the pool will always have at least minimum liquidity to provide service if all the liquidity providers burn their liquidity.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

