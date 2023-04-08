open class Coconet {
    protected val chiku = "brown"
    protected fun mData(){
        println("this is Coconet")
    }
}
// internal is not inherit
class Watermelon: Coconet() {
    fun bData()
    {
        println(chiku) //this access
        mData() //this access
    }
}

fun main() {
    Watermelon().bData()
//    Watermelon().chiku  //not access
//    Watermelon().mData() //not access
}