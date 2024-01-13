import scala.io.Source


def hash (s: String): Int {
    var h: Int = 0
    for (i < s){
        h = (h + i.toInt()) * 17 % 256
    }
    return h
}

object Main extends App {
  var total = 0

  for (step <- Source.fromFile("15.txt").getLines().next().split(',')) {
    var v = 0
    v = hash(step)
    total += v
  }

  println(total)
}