fun main() {
    var programmer = object:Human {
        override fun think() {
            print("I am an example of Anonymous Inner Class ")
        }
    }
    programmer.think()
}
interface Human {
    fun think()
}