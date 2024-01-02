import scala.io.Source

object Main extends App {
  def isValidArrangement(record: String, expectedGroupSizes: List[Int]): Boolean = {
    val actualGroups = "#+".r.findAllIn(record).toList
    val actualGroupSizes = actualGroups.map(_.length)
    actualGroupSizes == expectedGroupSizes
  }

  val inputFileName = "12.txt"
  val inputLines = Source.fromFile(inputFileName).getLines().toList

  var totalArrangements = 0

  for (line <- inputLines) {
    val Array(record, groups) = line.split(" ")
    val groupSizes = groups.split(",").map(_.toInt).toList

    val totalSprings = groupSizes.sum
    val unassignedSprings = totalSprings - record.count('#')
    val unassignedPositions = record.zipWithIndex.filter(_._1 == '?').map(_._2)

    var arrangementsCounter = 0

    for (assignment <- unassignedPositions.combinations(unassignedSprings)) {
      val newRecord = record.toArray
      for (position <- assignment) {
        newRecord(position) = '#'
      }
      if (isValidArrangement(newRecord.mkString, groupSizes)) {
        arrangementsCounter += 1
      }
    }

    totalArrangements += arrangementsCounter
  }

  println(totalArrangements)
}