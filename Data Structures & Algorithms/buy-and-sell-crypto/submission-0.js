class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let bestProfit = -Infinity

        for (let i = 0; i<prices.length; i++) {
            for (let j = i + 1; j < prices.length; j++) {
                let testPrice = prices[j] - prices[i]
                console.log(testPrice)
                if (testPrice > bestProfit) {
                    bestProfit = testPrice
                }
            }
        }
        if (bestProfit < 0) {
            bestProfit = 0
        }
        return bestProfit

    }
}
