package main

import (
	"fmt"
)

func main() {
	// 基本数据类型的变量：内存的一段空间

	var i int = 10
	fmt.Println(&i)

	// 指针类型 指针变量存的是一个地址，这个地址指向的空间 存的才是指
	//获取指针的类型所指向的值
	var ptr *int = &i

	fmt.Println(ptr)
	fmt.Println(*ptr)
	fmt.Println(&ptr)
}
