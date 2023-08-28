import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val queue: Queue<Int> = LinkedList<Int>()
    for (i in 1 .. n) {
        queue.add(i)
    }
    while (queue.size > 1) {
        queue.poll()
        queue.add(queue.poll())
    }
    println(queue.first())
}