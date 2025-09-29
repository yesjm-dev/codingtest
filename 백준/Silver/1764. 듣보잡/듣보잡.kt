import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val names = mutableMapOf<String, Int>()
    repeat(n + m) {
        val name = reader.readLine()
        if (names[name] != null) {
            names[name] = names.getOrDefault(name, 0) + 1
        } else {
            names[name] = 1
        }
    }

    val sb = StringBuilder()
    names.filter { it.value > 1 }
        .toSortedMap()
        .also {
            sb.append(it.size).append("\n")
            it.forEach { (key, _) -> sb.append(key).append("\n") }
        }

    println(sb)
}
