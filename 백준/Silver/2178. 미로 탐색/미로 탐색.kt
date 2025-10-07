import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val graph = Array(n) { reader.readLine().map { it - '0' }.toIntArray() }
    val visited = Array(n) { BooleanArray(m) }
    val dist = Array(n) { IntArray(m) }

    val dx = intArrayOf(1, -1, 0, 0)
    val dy = intArrayOf(0, 0, 1, -1)

    val queue: Queue<Pair<Int, Int>> = LinkedList()
    queue.add(Pair(0, 0))
    visited[0][0] = true
    dist[0][0] = 1

    while (queue.isNotEmpty()) {
        val (x, y) = queue.remove()
        for (i in 0..<4) {
            val nx = x + dx[i]
            val ny = y + dy[i]
            if (nx in 0 until n && ny in 0 until m) {
                if (!visited[nx][ny] && graph[nx][ny] == 1) {
                    visited[nx][ny] = true
                    dist[nx][ny] = dist[x][y] + 1
                    queue.add(Pair(nx, ny))
                }
            }
        }
    }

    println(dist[n - 1][m - 1])
}