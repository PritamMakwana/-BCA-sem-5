

// by default public
class X {
    var int = 10
}

// specified with public modifier
public class Y {
    var int = 20
    fun display() {
        println("Accessible everywhere")
    }
}
fun main(){
    println("x value is " +X().int)
    println("y value is " +Y().int)
    Y().display()
}
