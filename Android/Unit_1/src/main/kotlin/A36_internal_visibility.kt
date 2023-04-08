open class Apple {
    internal val chiku = "brown"
    internal fun mData(){
        println("this is Apple")
    }
}
// internal is not inherit
class Banana: Apple() {
    fun bData()
    {
        println(chiku) //this access
        mData() //this access
    }
}

fun main() {
   Banana().bData()
}