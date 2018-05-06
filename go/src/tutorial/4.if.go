package main

import "fmt"

func printX(x int) {
	if x > 10 {
		fmt.Println("x is greater than 10")
	} else {
		fmt.Println("x is less than or equals 10")
	}
}

//Go的if还有一个强大的地方就是条件判断语句里面允许声明一个变量，这个变量的作用域只能在该条件逻辑块内，其他地方就不起作用了

func computer() {
	// 计算获取值x,然后根据x返回的大小，判断是否大于10。
	if x := computedValue(); x >= 10 {
		fmt.Println("x is greater than or equals 10")
	} else {
		fmt.Println("x is less than 10")
	}

	//这个地方如果这样调用就编译出错了，因为x是条件里面的变量
	fmt.Println(x)
}

func computedValue() int {
	return 10
}
