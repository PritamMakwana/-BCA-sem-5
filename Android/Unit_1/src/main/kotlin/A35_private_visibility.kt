private class Z {
    private var d = 10
   private fun data(){
        println("this data only Z")
    }
}

// class X : Z() {
//} Z class is private
fun main(){
   // Z().data() //this is private method
   //print(Z().d) //var d is private
}
