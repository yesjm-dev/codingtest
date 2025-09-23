import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val n = reader.readLine().toInt()
    val nums = IntArray(n) { reader.readLine().toInt() }
    nums.sorted().forEach { println(it) }
}
