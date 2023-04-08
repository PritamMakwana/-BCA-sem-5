fun main() {
    val Human = Human1("pritam", 20)
    println(Human.message+Human.firstName+
            " Welcome to the example of Secondary constructor, Your Age is-"+Human.age)
}
class Human1(val firstName: String, var age: Int) {
    var message:String = "Hey!!!"
    constructor(name : String , age :Int ,message :String):this(name,age) {
        this.message = message
    }

}