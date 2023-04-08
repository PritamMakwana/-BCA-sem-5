open class Anum{
   open var n = 10
}
class Counter : Anum() {
    var count = 0
    override var n = 1
    fun incrementCount() {
        this.count += 2
    }
    fun exSuper(){
        println("n value in this class " + n)
        println("n value in Anum clas " + super.n)
    }
}
fun main() {
    var c: Counter = Counter()
    var count = 50
    c.incrementCount()
    println("count in main " + count)
    println("count in counter " + c.count)
    c.exSuper()
}