import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.collections.ArrayDeque

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val numbers = StringTokenizer(reader.readLine()).let {
        IntArray(m) { _ -> it.nextToken().toInt() }
    }

    val deque = ArrayDeque<Int>()
    for (i in 1..n) {
        deque.addLast(i)
    }

    var count = 0
    for (num in numbers) {
        val index = deque.indexOf(num)
        if (index <= deque.size / 2) {
            repeat(index) {
                deque.addLast(deque.removeFirst())
                count++
            }
        } else {
            repeat(deque.size - index) {
                deque.addFirst(deque.removeLast())
                count++
            }
        }
        deque.removeFirst()
    }
    println(count)
}