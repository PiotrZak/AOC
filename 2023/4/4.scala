import scala.io.Source

object LotteryGame {
  def main(args: Array[String]): Unit = {
    val source = Source.fromFile("4.txt")
    val cards = source.getLines().toArray
    source.close()

    var points = 0

    for (card <- cards) {
      val Array(win, lottery) = card.split('|')
      val Array(cardNumber, winNumbers) = win.split(":").map(_.trim)

      val winNums = "\\d+".r.findAllIn(winNumbers).map(_.toInt).toSet
      val lotteryNums = "\\d+".r.findAllIn(lottery).map(_.toInt).toSet

      val luckyCommon = winNums.intersect(lotteryNums)

      if (luckyCommon.nonEmpty) {
        points += math.pow(2, luckyCommon.size - 1).toInt
      }
    }

    println(points)
  }
}