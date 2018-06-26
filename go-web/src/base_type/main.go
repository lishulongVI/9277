package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	s = "this is string"
	fmt.Printf("%q\n", s)
	a := 10
	var b float64 = 23.456
	var c bool = true
	var mychar byte = 'h'

	fmt.Println(fmt.Sprintf("%d", a))

	fmt.Println(fmt.Sprintf("a type %T a = %d", a, a))

	fmt.Println(fmt.Sprintf("a type %T a = %f", b, b))
	fmt.Println(fmt.Sprintf("a type %T a = %c", mychar, mychar))
	fmt.Println(fmt.Sprintf("a type %T a = %t", c, c))
	var str string

	str = strconv.FormatInt(int64(a), 10)
	fmt.Println(str)
	str = strconv.FormatFloat(b, 'f', 10, 64)
	fmt.Println(str)

	fmt.Printf("%q\n", strconv.FormatBool(c))
	fmt.Printf("%q\n", strconv.FormatUint(uint64(mychar), 8))

}
