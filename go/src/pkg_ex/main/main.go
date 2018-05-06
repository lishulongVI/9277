package main

import (
	"fmt"
	"pkg/calc"
)

func main() {
	sum := calc.Add(1, 3)
	sub := calc.Sub(1, 3)

	fmt.Println(sum)
	fmt.Println(sub)
}
