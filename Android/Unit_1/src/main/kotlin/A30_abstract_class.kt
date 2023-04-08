abstract class Person() {
    fun displaySSN(ssn: Int) {
        println(" SSN is $ssn.")
    }
    abstract fun displayJob(description: String)
}
class Teacher: Person() {
    override fun displayJob(description: String) {
        println(description)
    }
    fun displayName(posi: String) {
        println("My positon is $posi.")
    }
}
fun main(){
    val t = Teacher()
    t.displayName("Admin")
    t.displayJob("Full control TO managment")
    t.displaySSN(229)
}