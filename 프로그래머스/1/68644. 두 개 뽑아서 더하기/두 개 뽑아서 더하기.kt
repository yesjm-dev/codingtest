class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()

        for (i in numbers.indices) {
            for (j in i + 1 until numbers.size) {
                answer += numbers[i] + numbers[j]
            }
        }

        return answer.sorted().distinct().toIntArray()
    }
}