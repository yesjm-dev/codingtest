import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val t = reader.readLine().toInt()

    val sb = StringBuilder()
    repeat(t) {
        val ps = reader.readLine()
        var count = 0
        var isValid = true
        for (s in ps) {
            if (s == '(') count++ else count--
            if (count < 0) {
                isValid = false
                break
            }
        }

        if (isValid && count == 0) {
            sb.append("YES\n")
        } else {
            sb.append("NO\n")
        }
    }

    println(sb)
}
