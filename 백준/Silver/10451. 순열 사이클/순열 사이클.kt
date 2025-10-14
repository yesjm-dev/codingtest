import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val sb = StringBuilder()
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val t = reader.readLine().toInt()
    repeat(t) {
        val n = reader.readLine().toInt()
        val st = StringTokenizer(reader.readLine())
        val arr = IntArray(n + 1)
        val visited = BooleanArray(n + 1)
        for (i in 1..n) {
            arr[i] = st.nextToken().toInt()
        }

        var count = 0
        for (i in 1..n) {
            if (!visited[i]) {
                dfs(arr, i, visited)
                count++
            }
        }
        sb.append("$count\n")
    }
    println(sb)
}

fun dfs(graph: IntArray, start: Int, visited: BooleanArray) {
    visited[start] = true
    val next = graph[start]
    if (!visited[next]) {
        dfs(graph, next, visited)
    }
}