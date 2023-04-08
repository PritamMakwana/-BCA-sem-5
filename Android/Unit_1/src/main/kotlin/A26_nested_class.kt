fun main() {
    val demo = Outer1().Nested().foo()
    print(demo)
}
class Outer1 {
    inner class Nested {
        fun foo() = "Welcome to kotlin"
    }
}