import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()
    val m = st.nextToken().toInt()

    val pocketmonNum = mutableMapOf<Int, String>()
    val pocketmonName = mutableMapOf<String, Int>()
    for (i in 1..n) {
        val name = reader.readLine()
        pocketmonNum[i] = name
        pocketmonName[name] = i
    }

    repeat(m) {
        val q = reader.readLine()
        if (q[0].isDigit()) {
            println(pocketmonNum[q.toInt()])
        } else {
            println(pocketmonName[q])
        }
    }
}