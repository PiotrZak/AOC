import scala.io.Source

object MirrorPos {
  def mirrorpos(arr: Array[Array[Int]], axis: Int = 0, diff: Int = 0): Int = {
    var m = arr.map(_.map(_.toInt))
    if (axis == 1) {
      m = m.transpose
    }
    for (i <- 0 until m.length - 1) {
      val upperFlipped = m.slice(0, i + 1).map(_.reverse)
      val lower = m.slice(i + 1, m.length)
      val rows = math.min(upperFlipped.length, lower.length)
      if (upperFlipped.take(rows).deep == lower.take(rows).deep) {
        return i + 1
      }
    }
    0
  }

  def main(args: Array[String]): Unit = {
    val fileName = "13.txt"
    val source = Source.fromFile(fileName)
    val data = source.mkString.split("\n\n")
    source.close()

    for (i <- 0 until 2) {
      var total = 0
      for (puzzle <- data) {
        val arr = puzzle.split("\n").map(_.replaceAllLiterally(".", "0").replaceAllLiterally("#", "1").map(_.toInt).toArray)
        total += 100 * mirrorpos(arr, axis = 0, diff = i) + mirrorpos(arr, axis = 1, diff = i)
      }
      println(total)
    }
  }
}