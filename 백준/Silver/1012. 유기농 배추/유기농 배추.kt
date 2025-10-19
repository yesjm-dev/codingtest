import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val t = reader.readLine().toInt()
    repeat(t) {
        val (m, n, k) = reader.readLine().split(" ").map { it.toInt() }
        val visited = Array(n) { IntArray(m) { 0 } }
        repeat(k) {
            val (x, y) = reader.readLine().split(" ").map { it.toInt() }
            visited[y][x] = 1
        }

        var count = 0
        for (i in 0 until n) {
            for (j in 0 until m) {
                if (visited[i][j] == 1) {
                    dfs(j, i, visited)
                    count ++
                }
            }
        }

        println(count)
    }
}

fun dfs(x: Int, y: Int, visited: Array<IntArray>) {
    visited[y][x] = 0

    val dx = arrayOf(0, 0, 1, -1)
    val dy = arrayOf(1, -1, 0, 0)

    for (i in 0 until 4) {
        val nx = x + dx[i]
        val ny = y + dy[i]
        if (ny in visited.indices && nx in visited[0].indices && visited[ny][nx] == 1) {
            dfs(nx, ny, visited)
        }
    }
}