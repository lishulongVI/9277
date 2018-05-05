package main

import (
	"fmt"
	"time"
)

func add(a int, b int) int {
	var sum int
	sum = a + b
	return sum
}

// Go 程序可以由多个标记组成，可以是关键字，标识符，常量，字符串，符号。如以下 GO 语句由 6 个标记组成：
func main() {
	go fmt.Println(add(100, 300))
	var a = 2
	fmt.Print(a)
	fmt.Println("hello HanBo")
	go test_goroute(100, 200)

	for i := 1; i <= 100; i++ {
		go fmt.Println(i)
	}
	time.Sleep(time.Second)
}

/***
➜  goroute git:(master) ✗ go run cal.go index.go
2hello HanBo
400
300

**/
