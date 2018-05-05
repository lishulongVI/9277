package main

import (
	"fmt"
	"time"
)

func test_pipe() {
	pipe := make(chan int, 3)
	pipe <- 1
	pipe <- 2
	pipe <- 3

	fmt.Println(len(pipe))

	t1 := <-pipe
	fmt.Println(t1)
	var t2 int
	t2 = <-pipe
	fmt.Println(t2)
}

func calculate(a int, b int) (int, int) {
	sum := a + b
	avg := sum / 2
	return sum, avg
}

func main() {
	test_pipe()
	time.Sleep(time.Second)

	sum, avg := calculate(1, 2)

	fmt.Println(sum, avg)

}
