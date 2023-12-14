#generated for chatgpt for analysis and learning scala.


import scala.io.Source
import scala.util.matching.Regex

object Main extends App {
  val st = System.currentTimeMillis()

  val lines = Source.fromFile("1test.txt").getLines().toList

  var totalSum = 0

  // Combine the regex pattern and compile it for better performance
  val pattern: Regex = """(\d)""".r

  for (row <- lines) {
    val numbers = pattern.findAllIn(row).toList
    if (numbers.nonEmpty) {
      totalSum += (numbers.head + numbers.last).toInt
    }
  }

  val et = System.currentTimeMillis()
  val elapsedTime = (et - st) / 1000.0
  println(s"Execution time: $elapsedTime seconds")
  println(s"Total sum: $totalSum")
}