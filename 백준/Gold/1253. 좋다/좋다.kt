fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val arr = readLine().split(" ").map { it.toInt() }.sorted()
    var count = 0
    repeat(n) { k ->
        var (find, i, j) = listOf(arr[k], 0, n - 1)
        while (i < j) {
            if (arr[i] + arr[j] == find) {
                if (i != k && j != k) {
                    count++
                    break
                } else if (i == k) {
                    i++
                } else if (j == k) {
                    j--
                }
            }
            else if (arr[i] + arr[j] < find) {
                i++
            }
            else {
                j--
            }
        }
    }
    println(count)
}