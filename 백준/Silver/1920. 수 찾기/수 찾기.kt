import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))

    val n = reader.readLine().toInt()
    val nList = reader.readLine().split(" ").map { it.toInt() }.sorted()

    val m = reader.readLine().toInt()
    val mList = reader.readLine().split(" ").map { it.toInt() }

    val sb = StringBuilder()
    for (i in mList) {
        val result = if (binarySearch(nList, i)) 1 else 0
        sb.append("$result\n")
    }
    print(sb)
}

fun binarySearch(arr: List<Int>, target: Int): Boolean {
    var left = 0
    var right = arr.size - 1

    while (left <= right) {
        val mid = left + (right - left) / 2
        when {
            arr[mid] == target -> return true
            arr[mid] < target -> left = mid + 1
            else -> right = mid - 1
        }
    }
    return false
}