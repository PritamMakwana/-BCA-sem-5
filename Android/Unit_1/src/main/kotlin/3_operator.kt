
fun main(args: Array<String>) {
    Arithmetic()
    Relational()
    Assignment()
    Unary()
    Logical()
}
fun Arithmetic(){
    var x: Int = 40
    var y: Int = 20

    println("1.Arithmetic Operators")
    println("x + y = " +  (x + y))
    println("x - y = " +  (x - y))
    println("x / y = " +  (x / y))
    println("x * y = " +  (x * y))
    println("x % y = " +  (x % y))
}
fun Relational(){
    val x: Int = 40
    val y: Int = 20
    println("2.Relational Operators")
    println("x > y = " +  (x > y))
    println("x < y = " +  (x < y))
    println("x >= y = " +  (x >= y))
    println("x <= y = " +  (x <= y))
    println("x == y = " +  (x == y))
    println("x != y = " +  (x != y))
}
fun Assignment(){
//    10=2-10
//    20=10
    println("3.Assignment Operators")
    var a = 10
    var b = 5
    a+=b
    println("a+=b " + a)
    a = 10
    a-=b
    println("a-=b " + a)
    a = 10

    a*=b
    println("a*=b " + a)
    a = 10

    a/=b
    println("a/=b " + a)
    a = 10

    a%=b
    println("a%=b " + a)
    a = 10

}
fun Unary() {
    println("4.Unary Operators")
    var x: Int = 40
    var b: Boolean = true

    println("+x = " + (+x))
    println("-x = " + (-x))
    println("++x = " + (++x))
    println("--x = " + (--x))
    println("!b = " + (!b))
}

fun Logical(){
    println("5.Logical Operators")
    var x: Boolean = true
    var y:Boolean = false

    println("x && y = " +  (x && y))
    println("x || y = " +  (x || y))
    println("!y = " +  (!y))
}
