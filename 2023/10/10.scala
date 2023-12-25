import scala.io.Source

object PipeMaze {
  def main(args: Array[String]): Unit = {
    // Read the file and process the data
    val data = Source.fromFile("10.txt").getLines().map(line => '.' + line + '.').toList
    val maze = data.head.indices.map(_ => '.').toList +: data :+ data.head.indices.map(_ => '.').toList

    // Define directions
    val directions = Map(
      'F' -> (0 + 1i, 1 + 0i),
      '7' -> (-1 + 0i, 0 + 1i),
      'J' -> (0 - 1i, -1 + 0i),
      'L' -> (1 + 0i, 0 - 1i),
      '-' -> (1 + 0i, -1 + 0i),
      '|' -> (0 + 1i, 0 - 1i),
      '.' -> (0i, 0i)
    )

    // Create the maze
    val mazeMap = collection.mutable.Map[Complex, Char]()
    val start = for {
      h <- maze.indices
      w <- maze.head.indices
      if maze(h)(w) == 'S'
    } yield Complex(w, h)

    val startPosition = start.head
    maze.indices.foreach { h =>
      maze.head.indices.foreach { w =>
        mazeMap(Complex(w, h)) = maze(h)(w)
      }
    }

    // Function to get neighbors
    def getNeighs(z: Complex): List[Complex] =
      if (mazeMap(z) != 'S') directions(mazeMap(z)).map(z + _).toList
      else List(z + (1 + 0i), z + (-1 + 0i), z + (1 + 1i), z + (-1 + 1i), z + (1 - 1i), z + (-1 - 1i), z + (0 + 1i), z + (0 - 1i))
        .filter(neighbor => z == directions(mazeMap(neighbor)).map(neighbor + _).contains(z))

    // Explore the maze
    var cur = getNeighs(startPosition).head
    var path = Set(cur)

    while (true) {
      val newNeighbors = getNeighs(cur).filterNot(path.contains)
      if (newNeighbors.nonEmpty) {
        path += newNeighbors.head
        cur = newNeighbors.head
      } else {
        break
      }
    }

    // Output the result
    println(path)
    println(path.size / 2)
  }
}

// Complex number class for representing positions
case class Complex(real: Int, imag: Int) {
  def +(other: Complex): Complex = Complex(real + other.real, imag + other.imag)
  def -(other: Complex): Complex = Complex(real - other.real, imag - other.imag)
}