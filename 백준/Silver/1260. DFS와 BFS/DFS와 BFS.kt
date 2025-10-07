import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

val sb = StringBuilder()

fun dfs(graph: Array<MutableList<Int>>, start: Int, visited: BooleanArray) {
    visited[start] = true
    sb.append("$start ")

    for (next in graph[start]) {
        if (!visited[next]) {
            dfs(graph, next, visited)
        }
    }
}

fun bfs(graph: Array<MutableList<Int>>, start: Int, visited: BooleanArray) {
    val queue: Queue<Int> = LinkedList()
    queue.add(start)
    visited[start] = true

    while (queue.isNotEmpty()) {
        val node = queue.poll()
        sb.append("$node ")

        for (next in graph[node]) {
            if (!visited[next]) {
                queue.add(next)
                visited[next] = true
            }
        }
    }
}

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()
    val v = st.nextToken().toInt()

    val graph = Array(n + 1) { mutableListOf<Int>() }
    repeat(m) {
        val (a, b) = reader.readLine().split(" ").map { it.toInt() }
        graph[a].add(b)
        graph[b].add(a)
    }
    for (i in 1..n) {
        graph[i].sort() // 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
    }

    var visited = BooleanArray(n + 1) { false }
    dfs(graph, v, visited)
    sb.append("\n")

    visited = BooleanArray(n + 1) { false }
    bfs(graph, v, visited)

    println(sb)
}