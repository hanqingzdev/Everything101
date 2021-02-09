/*
Purpose of this hello101.go:
1. Examples of using control statements;
2. Examples of functions;
3. Simple show cases of using primitives and basic data structures;

https://golang.org/ref/spec
*/

package main

import (
	"fmt"
	"reflect"
	//"time"

	"github.com/bradfitz/iter"
)

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
	ii, ff, bb := 0, float64(2)/5, 4 > 1
	fmt.Printf("Data type: Shart declared ii = %v, ff = %v, bb = %v\n", ii, ff, bb)
}

func dataTypeShowCaseTypes() {
	arrayTypes()
	sliceTypes()
	//structTypes()
	//pointerTypes()
	//functionTypes()
	//interfaceTypes()
	//mapTypes()
	//channelTypes()
}

func arrayTypes() {
	// array https://golang.org/ref/spec#Array_types
	/*
		- Arrays are values, just like int.
		- Assigning one array to another copies all the elements.
		- Passing an array to an function, it will receive a copy.
		- Size of an array is part of array. [10]int != [20]int
	*/
	var arr1 [5]int
	arr1[0] = 1
	arr1[1] = 2
	arr1[2] = 3
	arr1[3] = 4
	arr1[4] = 5
	arr2 := [5]int{1, 2, 3, 4, 5}
	var arr3 [6]int
	for i := range iter.N(5) {
		arr3[i] = i + 1
	}
	fmt.Printf("Array data type declared:\n\tarr1 = %v\n\tarr2 = %v\n\tarr3 = %v\n", arr1, arr2, arr3)
	fmt.Printf("\tarr1 == arr2: %v\n", arr1 == arr2)
	fmt.Printf("\tType of arr1: %v; arr3: %v\n", reflect.TypeOf(arr1), reflect.TypeOf(arr3))
	fmt.Printf("\t'arr1 == arr3' will get 'mismatched types' error\n")
	fmt.Printf("Go doesn't support negative index. 'arr1[-1]' will get 'index must be non-negative' error.\n")

	// 2D array
	var arr2d1 [3][3]int
	n := 1
	for i := range iter.N(3) {
		for j := range iter.N(3) {
			arr2d1[i][j] = n
			n++
		}
	}
	fmt.Printf("2D Array generated:\n")
	for i := range iter.N(3) {
		fmt.Printf("\t%v\n", arr2d1[i])
	}

	arr2d2 := [3][3]int{{9, 8, 7}, {6, 5, 4}, {3, 2, 1}}
	fmt.Printf("Another 2D Array declared:\n")
	for i := range iter.N(3) {
		fmt.Printf("\t%v\n", arr2d2[i])
	}
}

// https://play.golang.org/p/NeGuDahW2yP
func GetFibonacciFunction() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

func sliceTypes() {
	// https://golang.org/ref/spec#Slice_types
	var slice1 []int
	fmt.Printf("Slice slice1 declared: length: %v; capacity: %v\n", len(slice1), cap(slice1))
	slice2 := make([]int, 3, 10)
	fmt.Printf("Slice slice2 declared: length: %v; capacity: %v\n", len(slice2), cap(slice2))
	slice3 := new([100]int)[0:50]
	fmt.Printf("Slice slice3 declared: length: %v; capacity: %v\n", len(slice3), cap(slice3))

	// https://golang.org/ref/spec#Slice_expressions
	fi := GetFibonacciFunction()
	fibonacci := []int{fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi()}
	fmt.Printf("The fibonacci slice is: %v\n", fibonacci)
	fmt.Printf("\tlength: %v; capacity: %v\n", len(fibonacci), cap(fibonacci))
	fmt.Printf("The first 3 fibonacci numbers are: %v\n", fibonacci[:3])
	fmt.Printf("The last 3 fibonacci numbers are: %v\n", fibonacci[7:])
	fmt.Printf("The 3rd to 6th fibonacci numbers are: %v\n", fibonacci[2:6])

	// https://golang.org/ref/spec#Appending_and_copying_slices
	fi = GetFibonacciFunction() // reset fibonacci function
	fibonacci = make([]int, 3, 5)
	fibonacci[0] = fi()
	fibonacci[1] = fi()
	fibonacci[2] = fi()
	// fibonacci[3] = fi() // index out of range [3] with length 3
	fmt.Printf("The new fibonacci slice is made: %v. length: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))
	s1 := append(fibonacci, fi())
	fmt.Printf("\tAppend 1 value to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", s1, len(s1), cap(s1))
	s2 := append(s1, fi())
	fmt.Printf("\tAppend 1 value to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", s2, len(s2), cap(s2))
	s3 := append(s2, fi())
	fmt.Printf("\tAppend 1 value to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", s3, len(s3), cap(s3))
	s4 := append(s3, fi())
	fmt.Printf("\tAppend 1 value to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", s4, len(s4), cap(s4))
	fmt.Printf("\tThe original fibonacci slice is %v\n\tlength: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))

	// Reset
	fi = GetFibonacciFunction() // reset fibonacci function
	fibonacci = make([]int, 3, 6)
	fibonacci[0] = fi()
	fibonacci[1] = fi()
	fibonacci[2] = fi()
	fmt.Printf("Reset the fibonacci slice: %v\n\tlength: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))
	fibonacci = append(fibonacci, fi())
	fmt.Printf("\tAppend 1 value to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))
	fibonacci = append(fibonacci, fi(), fi(), fi())
	fmt.Printf("\tAppend 3 values to the slice:\n\t\t%v\n\t\tlength: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))

}

func mapTypes() {
	//numberMap := make(map[string]int, 100)
}
