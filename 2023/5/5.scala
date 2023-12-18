import scala.io.Source

val Array(seedsString, mappings @ _*) = Source.fromFile("5test.txt").mkString.split("\n\n")
val seeds = seedsString.split(" ").drop(1).map(_.toInt)

def lookup(start: Int, mapping: String): Int = {
  println(start)
  val lines = mapping.split("\n").tail
  for (line <- lines) {
    val Array(dst, src, len) = line.split(" ").map(_.toInt)
    val delta = start - src
    if (delta >= 0 && delta < len) {
      return dst + delta
    }
  }
  start
}

val result = seeds.map(s => mappings.foldLeft(s.toInt)(lookup))
println(result.min)
