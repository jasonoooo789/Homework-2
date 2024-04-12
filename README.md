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

The initial amounts of tokens(tokenA and tokenB) and the liquidity are:
$$x*y=k$$
Assume there are 2 transactions want to swap the same amount $x'$ of tokenA for tokenB. \
The first transaction:
$$(x+x')*(y-y')=k$$
$$y'=y-\frac{k}{(x+x')}$$
The second transaction:
$$(x+2x')*(y-y'-y'')=k$$
$$y''=y-y'-\frac{k}{(x+2x')}$$
Therefore,
$$y''\lt y'$$
Slippage is the price difference due to the tokens amount difference in the pool.
Uniswap V2 let users set a tolerence of every transaction. If the price exceeds the users' tolerence, the transaction will be reverted.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

It helps prevent potential manipulation of the liquidity pool. Without a minimum liquidity requirement, users could theoretically create tiny liquidity positions that could be easily manipulated or drained, leading to instability in the market.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

By ensuring that the product of the quantities of the two tokens remains constant, the constant product formula helps maintain relative price stability between the tokens in the liquidity pool. Moreover, The formula prevents users from manipulating the liquidity pool by depositing disproportionately large amounts of one token compared to the other. Any attempt to do so would result in an immediate adjustment of the liquidity shares, minimizing arbitrage opportunities.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

The attacker front-run a transaction before the victim's transaction and sell the tokens he gain from front-running after the victim's transaction finish. Thus, the attacker make the price difference between two transaction and the victim spends more for the same amount of tokens since the front-running transaction have increased the price.
