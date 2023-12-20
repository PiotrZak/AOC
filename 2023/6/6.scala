import scala.io.Source
import scala.util.matching.Regex

object Main extends App {
  val st = System.currentTimeMillis()

  val lines = Source.fromFile("6.txt").getLines().toArray
  val races = lines.collect {
    case line if line.nonEmpty =>
      line.split(":")(1).trim.split("\\s+").map(_.toInt)
  }

  val timeDistanceRacesPairs = races.transpose
  var recordsPerRace = List[Int]()

  for ((millisecond, millimeter) <- timeDistanceRacesPairs) {
    var record = 0

    for (hold <- 1 until millisecond) {
      val distance = hold * (millisecond - hold)

      if (distance > millimeter) {
        record += 1
      }
    }

    recordsPerRace = record :: recordsPerRace
  }

  val result = recordsPerRace.product
  println(result)

  val et = System.currentTimeMillis()
  val elapsedTime = (et - st) / 1000.0
  println(s"Execution time: $elapsedTime seconds")
}
