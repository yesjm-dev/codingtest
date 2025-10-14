import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val (m, n, k) = reader.readLine().split(" ").map { it.toInt() }
    val visited = Array(m) { BooleanArray(n) { false } }
    repeat(k) {
        val (x1, y1, x2, y2) = reader.readLine().split(" ").map { it.toInt() }
        for (i in y1 until y2) {
            for (j in x1 until x2) {
                visited[i][j] = true
            }
        }
    }

    val result = mutableListOf<Int>()
    for (i in 0 until m) {
        for (j in 0 until n) {
            if (!visited[i][j]){
                result.add(dfs(i, j, visited))
            }
        }
    }
    result.sort()

    println(result.size)
    println(result.joinToString(" "))
}

fun dfs(x: Int, y: Int, visited: Array<BooleanArray>): Int {
    var count = 1
    visited[x][y] = true
    
    val dx = arrayOf(0, 0, 1, -1)
    val dy = arrayOf(1, -1, 0, 0)
    
    for (i in 0 until 4) {
        val nx = x + dx[i]
        val ny = y + dy[i]
        if (nx in visited.indices && ny in visited[0].indices && !visited[nx][ny]) {
            count += dfs(nx, ny, visited)
        }
    }
    return count
}