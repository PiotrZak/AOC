import scala.io.Source

object ReflectCode {
  def main(args: Array[String]): Unit = {
    val file = Source.fromFile("./14.txt").getLines().toList

    var reflector = file.map(_.trim).toSeq

    def transpose(matrix: Seq[String]): Seq[String] = matrix.transpose.map(_.mkString)

    // Flip reflector
    reflector = transpose(reflector)

    for (i <- reflector.indices) {
      var groups = Seq[String]()
      // Sort reflector by splitting #
      for (group <- reflector(i).split("#")) {
        val newGroup = group.sorted(Ordering[Char].reverse)
        groups = groups :+ newGroup.mkString
      }
      reflector = reflector.updated(i, groups.mkString("#"))
    }

    // Flip reflector back
    reflector = transpose(reflector)

    var count = 0

    for ((row, i) <- reflector.reverse.zipWithIndex) {
      count += row.count(_ == 'O') * (i + 1)
    }

    println(count)
  }
}