package main

import "fmt"

var isActive bool                   // 全局变量声明
var enabled, disabled = true, false // 忽略类型的声明
func test() {
	var available bool // 一般声明
	valid := false     // 简短声明
	available = true   // 赋值操作

	fmt.Println(available)
	fmt.Println(valid)
}

func add(a int, b int) int {
	var sum int
	sum = a + b
	return sum
}

// Go 程序可以由多个标记组成，可以是关键字，标识符，常量，字符串，符号。如以下 GO 语句由 6 个标记组成：
func main() {
	var a = 2

	fmt.Print(a)

	fmt.Println("hello HanBo")

	test()

	fmt.Println(add(100, 300))
}
