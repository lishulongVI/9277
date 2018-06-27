package main

import (
	"fmt"
	"strconv"
)

func main() {

	// string 转基本数据类型

	var a int = 9999
	var str string

	str = strconv.Itoa(a)
	fmt.Println(str)

	str = "true"
	b, _ := strconv.ParseBool(str)

	fmt.Println(b)

	str = "1234567"
	c, _ := strconv.ParseFloat(str, 32)
	fmt.Println(c)

	cd, _ := strconv.ParseInt(str, 10, 32)
	fmt.Println(cd)
	str = "hello"
	cs, err := strconv.ParseInt(str, 10, 32)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(cs)

}
