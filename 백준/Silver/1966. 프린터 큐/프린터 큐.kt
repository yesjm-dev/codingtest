import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayDeque

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val t = reader.readLine().toInt()
    val sb = StringBuilder()

    repeat(t) {
        val st = StringTokenizer(reader.readLine())
        val n = st.nextToken().toInt()
        val m = st.nextToken().toInt()
        val st2 = StringTokenizer(reader.readLine())
        val deque = ArrayDeque<Pair<Int, Int>>()
        for (i in 0..<n) {
            deque.addLast(i to st2.nextToken().toInt())
        }
        var count = 0

        while (deque.isNotEmpty()) {
            val (index, priority) = deque.removeFirst()
            if (deque.any { it.second > priority }) {
                deque.addLast(index to priority)
            } else {
                count++
                if (index == m) {
                    sb.append("$count\n")
                    break
                }
            }
        }
    }

    println(sb)
}