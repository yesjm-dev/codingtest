import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val heights = reader.readLine().split(" ").map { it.toInt() }

    var low = 0L
    var high = heights.max().toLong()
    var answer = 0L

    while (low <= high) {
        val mid = (low + high) / 2
        var sum = 0L

        for (h in heights) {
            if (h > mid) {
                sum += (h - mid)
            }
        }

        if (sum >= m) {
            answer = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    println(answer)
}