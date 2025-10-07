import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val m = st.nextToken().toInt()
    val n = st.nextToken().toInt()
    val store = Array(n) { IntArray(m) }

    val dx = intArrayOf(1, -1, 0, 0)
    val dy = intArrayOf(0, 0, 1, -1)

    val queue: Queue<Pair<Int, Int>> = LinkedList()
    repeat(n) { i ->
        val line = StringTokenizer(reader.readLine())
        repeat(m) { j ->
            store[i][j] = line.nextToken().toInt()
            if (store[i][j] == 1) {
                queue.add(Pair(i, j))
            }
        }
    }

    while (queue.isNotEmpty()) {
        val (x, y) = queue.remove()

        for (i in 0 until 4) {
            val nx = x + dx[i]
            val ny = y + dy[i]

            if (nx in 0 until n && ny in 0 until m && store[nx][ny] == 0) {
                store[nx][ny] = store[x][y] + 1
                queue.add(Pair(nx, ny))
            }
        }
    }

    var result = 0
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (store[i][j] == 0) {
                println(-1)
                return
            }
            result = maxOf(result, store[i][j])
        }
    }

    println(result - 1)
}