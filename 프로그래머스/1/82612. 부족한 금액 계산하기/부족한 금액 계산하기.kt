class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var total: Long = 0
        for (i in 1..count) {
            val cost = price * i
            total += cost
        }
        return if (money < total) total - money
        else return 0
    }
}