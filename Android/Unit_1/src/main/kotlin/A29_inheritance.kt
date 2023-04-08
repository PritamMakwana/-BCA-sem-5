open class ParentClass {
    fun think () {
        print("Parent Class is thinking")
    }
}
class ChildClass: ParentClass()
fun main() {
    ChildClass().think()
}