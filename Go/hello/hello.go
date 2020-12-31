package main

import (
	"fmt"
	"hqzhang.dev/greetings"
)

func main() {
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}
