package main

import "fmt"

func switch_(i int) {
	switch i {
	case 1:
		fmt.Println("i is equal to 1")
	case 2, 3, 4:
		fmt.Println("i is equal to 2, 3 or 4")
	case 10:
		fmt.Println("i is equal to 10")
	default:
		fmt.Println("All I know is that i is an integer")
	}
}

func for_() {
	sum := 0
	for index := 0; index < 10; index++ {
		sum += index
	}
	fmt.Println("sum is equal to ", sum)

	map_ := make(map[string]string)
	map_["name"] = "李书龙"
	map_["age"] = "24"
	for k, v := range map_ {
		fmt.Println("map's key:", k)
		fmt.Println("map's val:", v)
	}
}
