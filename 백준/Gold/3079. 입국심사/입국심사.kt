import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val times = LongArray(n) { reader.readLine().toLong() }

    var low = 1L
    var high = m * times.max()
    var answer = high

    while (low <= high) {
        val mid = (low + high) / 2
        var sum = 0L

        for (t in times) {
            sum += mid / t
            if (sum >= m) {
                break
            }
        }

        if (sum >= m) {
            answer = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }

    println(answer)
}