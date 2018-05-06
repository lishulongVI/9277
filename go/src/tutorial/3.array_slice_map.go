package main

import (
	"fmt"
)

var arr [10]int // 声明了一个int类型的数组

func display() [10]int {
	arr[0] = 42 // 数组下标是从0开始的
	arr[1] = 13 // 赋值操作
	return arr
}

func slice() {
	// 声明一个数组
	var array = [10]byte{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
	// 声明两个slice
	var aSlice, bSlice []byte

	// 演示一些简便操作
	aSlice = array[:3] // 等价于aSlice = array[0:3] aSlice包含元素: a,b,c
	fmt.Println(aSlice)
	aSlice = array[5:] // 等价于aSlice = array[5:10] aSlice包含元素: f,g,h,i,j
	fmt.Println(aSlice)
	aSlice = array[:] // 等价于aSlice = array[0:10] 这样aSlice包含了全部的元素
	fmt.Println(aSlice)

	// 从slice中获取slice
	aSlice = array[3:7] // aSlice包含元素: d,e,f,g，len=4，cap=7
	fmt.Println(aSlice)
	bSlice = aSlice[1:3] // bSlice 包含aSlice[1], aSlice[2] 也就是含有: e,f
	fmt.Println(bSlice)
	bSlice = aSlice[:3] // bSlice 包含 aSlice[0], aSlice[1], aSlice[2] 也就是含有: d,e,f
	fmt.Println(bSlice)
	bSlice = aSlice[0:5] // 对slice的slice可以在cap范围内扩展，此时bSlice包含：d,e,f,g,h
	fmt.Println(bSlice)
	bSlice = aSlice[:] // bSlice包含所有aSlice的元素: d,e,f,g
	fmt.Println(bSlice)

	fmt.Println(len(bSlice))
	fmt.Println(cap(bSlice))

}

func map_() {
	// 声明一个key是字符串，值为int的字典,这种方式的声明需要在使用之前使用make初始化
	var numbers map[string]int
	// 另一种map的声明方式
	numbers = make(map[string]int)
	numbers["one"] = 1  //赋值
	numbers["ten"] = 10 //赋值
	numbers["three"] = 3

	fmt.Println("第三个数字是: ", numbers["three"]) // 读取数据
	// 打印出来如:第三个数字是: 3
}
