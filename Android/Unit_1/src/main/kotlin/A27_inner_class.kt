class outerClass{
    fun fooouter(){
        println("call outer class")
    }
    inner class  innerClass{
        fun fooInner(){
           println("call inner class")
        }
    }
}
fun main(){
    outerClass().fooouter()
    outerClass().innerClass().fooInner()
}