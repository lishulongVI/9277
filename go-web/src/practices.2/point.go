package main

import (
	"fmt"
)

func main() {
	var b string = `北京 \n 长城`
	fmt.Println(b)
	b = "北京 \n 长城"
	fmt.Println(b)

	str := `
	package main

	import (
		"fmt"
	)

	func main() {
		var b bool = false
		fmt.Println(b)
	}
	`
	fmt.Println(str)
}
