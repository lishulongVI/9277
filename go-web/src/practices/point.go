package main

import (
	"errors"
	"fmt"
)

func testPtr() {
	fmt.Println("こんにちはせかい!!!")
}

func test_valu() {
	var a int
	a = 10
	fmt.Println(a)

	var aa, bb, cc int = 1, 2, 3

	fmt.Println(aa)
	fmt.Println(bb)

	fmt.Println(cc)
	a, b, c := 11, 22, "33"
	fmt.Print(a, b, c)

	_, bbb := 23, 45
	fmt.Println(bbb)
	fmt.Println(bbb)

	const PI float64 = 3.14159926

	fmt.Print(PI)
}

func test_v_b() {

	var frenchHello string
	frenchHello = "hello french"

	var emptyString string = ""

	fmt.Println(frenchHello)
	fmt.Println(emptyString)
}

func test_s_v() {
	s := "hello"
	c := []byte(s)
	c[0] = 'c'
	fmt.Println(s)
	fmt.Printf("%s\n", c)

	s = string(c)
	fmt.Println(s == "cello")

	m := "hello"

	m = "C" + m[1:]
	fmt.Printf("%s\n", m)

}

func error_deal() {

	err := errors.New("emit macho dwarf")
	if err != nil {
		fmt.Println(err)
	}

}

func display() {
	const (
		i      = 199
		pi     = 2303003
		prefix = "go_"
	)

	var (
		iq      int
		piq     float32
		prefixq string
	)

	iq = 13
	piq = 3.3222
	prefixq = "go"

	fmt.Println(iq)
	fmt.Println(piq)
	fmt.Println(prefixq)
}

func ista_demo() {
	const (
		x = iota
		y = iota
		z = iota
		w
	)

	const v = iota

	const (
		e, f, g = iota, iota, iota
	)

}

//go 程序设计的一些规则
/***
大写字母开头的变量是可导出的 其他包可以读取是公用变量
小写字母开头的是私有变量
***/

func array_() {
	var arr [12]int
	arr[0] = 1
	fmt.Println(arr)

	a := [...]int{1, 2, 4}
	fmt.Println(a)
}

func main() {
	array_()
	// testPtr()
	// test_valu()
	// test_v_b()
	// test_s_v()
	// error_deal()
	// display()

}
