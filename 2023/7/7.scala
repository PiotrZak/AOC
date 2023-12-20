import scala.io.Source

object PokerHands {

  val cards = List('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

  def main(args: Array[String]): Unit = {
    val INPUT = "7test.txt"
    val hands = Source.fromFile(INPUT).getLines().map(line => {
      val Array(hand, value) = line.split(" ")
      (hand, value.toInt)
    }).toList

    println(hands)

    val key: ((String, Int)) => Int = hand => {
      val handCounts = hand._1.groupBy(identity).mapValues(_.length).values.toList.sorted.reverse
      val keyPart1 = handCounts.mkString("").padTo(5, '0')
      val keyPart2 = hand._1.map(card => "%02d".format(cards.indexOf(card) + 1)).mkString("")
      (keyPart1 + keyPart2).toInt
    }

    val sortedHands = hands.sortBy(key)
    val total = sortedHands.gigizipWithIndex.map { case (hand, index) =>
      (index + 1) * hand._2
    }.sum

    println(s"TOTAL $total")
  }
}