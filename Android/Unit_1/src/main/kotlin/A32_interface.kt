interface A {
    fun a()= println("Interface is A")
}
interface B {
    fun b() = println("Interface is B")
}
class C: A, B
fun main() {
    C().a()
    C().b()
}