/*
Purpose of this hello101.go:
1. Examples of using control statements;
2. Examples of functions;
3. Simple show cases of using primitives and basic data structures;

https://golang.org/ref/spec
*/

package main

import "fmt"

func main() {
	fmt.Println("Hello, World! 101!")

	basicStatements()
	functionShowCases()
	dataTypeShowCasePrimitives()
	dataTypeShowCaseTypes()
}

func basicStatements() {
	// if statement
	if 1 > 0 {
		fmt.Println("Sure, 1 > 0")
	}

	if x := 1; x > 0 {
		fmt.Println("Still, x > 0 (x = 1)")
	}

	// for statement
	sum := 0
	for i := 1; i <= 100; i++ {
		sum += i
	}
	fmt.Println("The sum from 1 to 100 is", sum)

	sum, i := 0, 1
	for i <= 100 {
		sum += i
		i++
	}
	fmt.Printf("Again, the sum from 1 to 100 is %d\n", sum)

	sum, i = 0, 1 // can NOT use ':=' since both `sum` and `i` are declared
	for {
		sum += i
		i++
		if i == 100 {
			break
		}
	}
	fmt.Printf("3rd time, the sum from 1 to %d is %d\n", i, sum)

	sum = 0
	numbers := []int{1, 2, 3, 4, 5}
	for x := range numbers {
		sum += x
	}
	fmt.Printf("The sum from %v is %d\n", numbers, sum) // https://golang.org/pkg/fmt/

	sum = 0
	numMap := map[string]int{"one": 1, "two": 2, "three": 3}
	for _, v := range numMap {
		sum += v
	}
	fmt.Printf("The sum of values of %v is %d\n", numMap, sum)

	// switch statement
	sum = 0
	numMap = map[string]int{"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
	pickMap := make(map[int]bool)
	for _, v := range numMap {
		switch {
		default:
			pickMap[v] = false
		case v%2 == 0 && v != 2:
			pickMap[v] = true
		case v == 2:
			pickMap[v] = false
		case v == 5:
			pickMap[v] = true
		case v == 1, v == 3:
			pickMap[v] = false
		}
	}
	for v, pick := range pickMap {
		switch {
		case pick:
			sum += v
		}
	}
	fmt.Printf("The sum of picked values %v is %d\n", pickMap, sum)

}

func functionShowCases() {
	var rst int

	rst = add(1, 2)
	fmt.Printf("Function 'add' gave me %d\n", rst)

	rst1, rst2 := addMinus(1, 2)
	fmt.Printf("Function 'addMinus' gave me %d, %d.\n", rst1, rst2)

	rst = addNamedReturns(1, 2)
	fmt.Printf("Function 'addNamedReturns' gave me %d\n", rst)

	fmt.Println("Function 'addDefaultParameterValue' is not supported. https://golang.org/doc/faq#overloading")

	rst = addDefer(1, 2)
	fmt.Printf("Function 'addDefer' gave me %d.\n", rst)

	rst = addMultiDefer(1, 2)
	fmt.Printf("Function 'addMiltiDefer' gave me %d.\n", rst)

	addVoid(1, 2)
	fmt.Println("Function 'addVoid' just being called")
}

func add(in1 int, in2 int) int {
	return in1 + in2
}

func addMinus(in1 int, in2 int) (int, int) {
	return in1 + in2, in1 - in2
}

func addDefer(in1 int, in2 int) int {
	defer fmt.Println("\taddDefer() is about to close.")
	fmt.Println("\taddDefer() is running.")
	return in1 + in2
}

func addMultiDefer(in1 int, in2 int) int { // LIFO
	defer fmt.Printf("\taddMultiDefer() saw in1 is %d.\n", in1)
	defer fmt.Printf("\taddMultiDefer() saw in2 is %d.\n", in2)
	defer fmt.Println("\taddMultiDefer() is about to close.")
	fmt.Println("\taddDefer() is running.")
	return in1 + in2
}

func addNamedReturns(in1 int, in2 int) (rst int) {
	rst = in1 + in2
	return
}

func addVoid(in1 int, in2 int) {
	fmt.Printf("\taddVoid() is getting %d.\n", in1+in2)
}

func dataTypeShowCasePrimitives() {
	// Data type: declaring primitives
	const (
		zero = iota
		one  = iota
		two  = iota
		_    // iota == 3, skipped
		four = iota
		five = iota
		six  = iota
	)

	// https://golang.org/ref/spec#Variable_declarations
	var i int
	var f float64
	var b bool
	i, f, b = zero, float64(two)/five, four > one
	fmt.Printf("Data type: Declared i = %v, f = %v, b = %v\n", i, f, b)

	// https://golang.org/ref/spec#Short_variable_declarations
	ii, ff, bb := zero, float64(two)/five, four > one
	fmt.Printf("Data type: Shart declared ii = %v, ff = %v, bb = %v\n", ii, ff, bb)
}

func dataTypeShowCaseTypes() {
	// array https://golang.org/ref/spec#Array_types
	/*
		- Arrays are values, just like int.
		- Assigning one array to another copies all the elements.
		- Passing an array to an function, it will receive a copy.
		- Size of an array is part of array. [10]int != [20]int
	*/
}

func arrayTypes() {
}

func mapTypes() {
	//numberMap := make(map[string]int, 100)
}
