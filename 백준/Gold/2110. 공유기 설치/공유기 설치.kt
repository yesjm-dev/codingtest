import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val c = st.nextToken().toInt()

    val houses = LongArray(n) { reader.readLine().toLong() }
    houses.sort()

    var low = 1L
    var high = houses.last() - houses.first()
    var answer = 0L

    while (low <= high) {
        val mid = (low + high) / 2
        var last = houses[0]

        var count = 1
        for (i in 1 until n) {
            if (houses[i] - last >= mid) {
                count++
                last = houses[i]
            }
        }

        if (count >= c) {
            answer = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    println(answer)
}