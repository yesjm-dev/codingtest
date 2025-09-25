import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val n = reader.readLine().toInt()
    val numbers = reader.readLine().split(" ").map { it.toInt() }

    val c = reader.readLine().toInt()

    var low = 0
    var high = numbers.max()
    var answer = 0

    while (low <= high) {
        val mid = (low + high) / 2 // 예산
        var sum = 0L // 예산의 합
        for (num in numbers) {
            sum += if (num > mid) mid else num
        }

        if (sum <= c) { // 예산이 넘지 않을때 올려볼 수 있음
            answer = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    println(answer)
}