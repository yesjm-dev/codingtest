class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = intArrayOf()

        for (command in commands) {
            val i = command[0]
            val j = command[1]
            val k = command[2]

            val subArray = array.slice(IntRange(i - 1, j - 1)).sorted()
            answer += subArray[k - 1]
        }

        return answer
    }
}