import scala.io.Source

object Main extends App {
  val st = System.currentTimeMillis()

  val network = Source.fromFile("8.txt").getLines().toSeq
  val direction = network.head.toCharArray
  val networkMap = network.tail.map(line => {
    val parts = line.split("[\\W]+")
    parts.head -> (parts(1), parts(2))
  }).toMap

  var start = "AAA"
  val finish = "ZZZ"
  var steps = 0
  var points = List[String]()

  while (true) {
    for (u <- direction) {
      steps += 1
      start = if (u == 'L') networkMap(start)._1 else networkMap(start)._2
      points :+= (if (u == 'L') networkMap(start)._1 else networkMap(start)._2)
      if (start == finish) {
        println(steps)
        println("This way according: " + points.mkString(", "))
        val et = System.currentTimeMillis()
        val elapsedTime = (et - st) / 1000.0
        println("Execution time: " + elapsedTime + " seconds")
        sys.exit()
      }
    }
  }
}