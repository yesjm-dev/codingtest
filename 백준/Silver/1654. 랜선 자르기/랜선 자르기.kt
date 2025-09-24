import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val k = st.nextToken().toInt()
    val n = st.nextToken().toInt()

    val cables = LongArray(k) { reader.readLine().toLong() }

    var low = 1L
    var high = cables.max()
    var answer = 0L

    while (low <= high) {
        val mid = (low + high) / 2
        var sum = 0L

        for (c in cables) {
            sum += (c / mid)
        }

        if (sum >= n) {
            answer = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    println(answer)
}