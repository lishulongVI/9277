package main

import (
	"fmt"
)

func main() {
	var i int32 = 134

	j := float32(i)

	k := int8(i)

	fmt.Println(j)
	fmt.Println(k)

	const (
		a = iota //0
		b        //1
		c        //2
		d = "ha" //独立值，iota += 1
		e        //"ha"   iota += 1
		f = 100  //iota +=1
		g        //100  iota +=1
		kk
		h  = iota //7,恢复计数
		jk        //8
	)
	fmt.Println(a, b, c, d, e, f, g, h, kk, jk)
}
