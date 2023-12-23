import scala.io.Source
import scala.math._

object PascalTriangle {
  def main(args: Array[String]): Unit = {
    val filename = "9.txt"

    val source = Source.fromFile(filename)
    val lines = source.getLines().toList
    source.close()

    var totalSum = 0

    for (line <- lines) {
      val formattedLine = line.split("\\s+").map(_.toInt)

      for ((value, index) <- formattedLine.zipWithIndex) {
        val pascal = binomial(formattedLine.length, index)
        totalSum += value * pascal * math.pow(-1, formattedLine.length - index + 1).toInt
      }
    }

    println(s"Total: $totalSum")
  }

  def binomial(n: Int, k: Int): Int = {
    factorial(n) / (factorial(k) * factorial(n - k))
  }

  def factorial(n: Int): Int = {
    if (n == 0 || n == 1) 1
    else n * factorial(n - 1)
  }
}