import scala.io.Source


object Galaxies {

    def findGalaxies(lines: Array[String]) : (Array[Int, Int]) = {

            val galaxies = for {
                (line, i) <- lines.zipWithIndex
                (char, j) <- line.zipWithIndex
                if char == '#'
            } yield (i, j)

            val space = for {
                (line, i) <- lines.zipWithIndex
                (char, j) <- line.zipWithIndex
                if char == '.'
            } yield (i, j)
            
            (galaxies, space)
        }

    def findEmptySpaces(lines: Array[String]): (Array[Int], Array[Int]) = {

        val emptyRows = lines.zipWithIndex.collect{
            case (line, i) if line.forAll(_ != '#') => i
        }

        val transposedLines = lines.transpose
        val emptyCols = transposedLines.zipWithIndex.collect{
            case (col, i) if col.forAll(_ != '#') => i
        }

        (emptyRows, emptyCols)
    }

    val (galaxies, space) = findGalaxies(lines)
    val (x, y) = findEmptySpaces(lines)


    def getGalaxyPairs(galaxies: Array[(Int, Int)]): Array[((Int, Int), (Int, Int))] = {
        val pairs = for {
            (galaxy, i) <- galaxies.zipWithIndex
            (otherGalaxy, j) <- galaxies.take(i)
            if i < j
        } yield (galaxy, otherGalaxy)
    }

    // Shortest path between pairs (functional approach)
    def shortestPathBetweenPairsFunctional(galaxyPairs: Array[((Int, Int), (Int, Int))], x: Array[Int], y: Array[Int]): Int = {
         
        // Calculate path between two galaxies (one pair) - then sum
        def calculatePath(galaxyPair: ((Int, Int), (Int, Int))): Int = {
            val ((galaxyRow, galaxyCol), (otherGalaxyRow, otherGalaxyCol)) = galaxyPair

            def calculateDimensionPath(min: Int, max: Int, coordinates: Array[Int]): Int =
            (min until max).map(coord => if (coordinates.contains(coord)) 2 else 1).sum

            calculateDimensionPath(math.min(otherGalaxyRow, galaxyRow), math.max(otherGalaxyRow, galaxyRow), x) +
            calculateDimensionPath(math.min(otherGalaxyCol, galaxyCol), math.max(otherGalaxyCol, galaxyCol), y)
        }

        galaxyPairs.map(calculatePath).sum
    }

    // Usage
    val result = shortestPathBetweenPairsFunctional(galaxyPairs, x, y)
    println(result)


}
