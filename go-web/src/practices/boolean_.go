package main

import "fmt"

var isActive = false

var enable, disable = true, true

func test1() {
	var available bool
	valid := false
	available = true

	fmt.Println(isActive)
	fmt.Println(available)
	fmt.Println(valid)
}

func test_test() {
	fmt.Println("hello ")
}
