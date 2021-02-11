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
	"math"
	"reflect"
	//s "strings"
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
	structTypes()
	pointerTypes()
	functionTypes()
	//interfaceTypes()
	//mapTypes()
	//channelTypes()
}

func arrayTypes() {
	// array https://golang.org/ref/spec#Array_types
	/*
		- Arrays are values, just like int.
		- It is NOT a pointer to the first array element.
		- Assigning one array to another copies all the elements.
		- Passing an array to an function, it will receive a copy.
		- Size of an array is part of array. [10]int != [20]int
		- Arrays do not need to be initialized explicitly; the zero value of an array is a ready-to-use.
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
	var arr4 [3]int
	arr5 := [...]int{1, 2, 3, 4}
	fmt.Printf("Array data type declared:\n\tarr1 = %v\n\tarr2 = %v\n\tarr3 = %v\n\tarr4 = %v\n", arr1, arr2, arr3, arr4)
	fmt.Printf("\tarr5 = %v\n", arr5)
	fmt.Println("\t======\n")
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
	/* A slice is a descriptor of an array segment. It consists:
	1. a pointer to the array element (first element of the slice),
	2. the length of the segment,
	3. its capacity (the maximum length of the segment, NOT the underlaying array).
	*/
	// https://golang.org/ref/spec#Slice_types
	fmt.Println("Declaring slices:")
	var slice1 []int
	fmt.Printf("\t'var slice1 []int': length: %v; capacity: %v\n", len(slice1), cap(slice1))
	slice2 := make([]int, 3, 10)
	fmt.Printf("\t'slice2 := make([]int, 3, 10)': length: %v; capacity: %v\n", len(slice2), cap(slice2))
	slice3 := new([100]int)[0:50]
	fmt.Printf("\t'slice3 := new([100]int)[0:50]':  length: %v; capacity: %v\n", len(slice3), cap(slice3))

	fi := GetFibonacciFunction()
	fibonacci := []int{fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi(), fi()}

	// https://golang.org/ref/spec#Slice_expressions
	fmt.Println("Slice expressions:")
	fmt.Printf("\tInit a fibonacci slice: %v\n", fibonacci)
	fmt.Printf("\tlength: %v; capacity: %v\n", len(fibonacci), cap(fibonacci))
	fmt.Printf("\t[:3] The first 3 fibonacci numbers are: %v\n", fibonacci[:3])
	fmt.Printf("\t[7:] The last 3 fibonacci numbers are: %v\n", fibonacci[7:])
	fmt.Printf("\t[2:6] The 3rd to 6th fibonacci numbers are: %v\n", fibonacci[2:6])
	fmt.Printf("\t[:]: %v\n", fibonacci[:])

	// Re-slicing
	// Case 1
	s := fibonacci[:4]
	fmt.Printf("Re-slicing. s = fibonacci[:4]: %v\n", s)
	s = fibonacci[:4]
	s = s[:5]
	fmt.Printf("\ts[:5]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	s = fibonacci[:4]
	s = s[:cap(s)]
	fmt.Printf("\ts[:cap(s)]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	s = fibonacci[:4]
	s = s[5:8]
	fmt.Printf("\ts[5:8]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	s = fibonacci[:4]
	s = s[:]
	fmt.Printf("\ts[:]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	// Case 2
	fmt.Printf("Re-slicing. s = fibonacci[2:5]: %v\n", s)
	s = fibonacci[2:5]
	s = s[:5]
	fmt.Printf("\ts[:5]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	s = fibonacci[2:5]
	s = s[:cap(s)]
	fmt.Printf("\ts[:cap(s)]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))
	s = fibonacci[2:5]
	s = s[3:cap(s)]
	fmt.Printf("\ts[3:cap(s)]: %v. length:%v; capacity:%v\n", s, len(s), cap(s))

	// https://golang.org/ref/spec#Appending_and_copying_slices
	fi = GetFibonacciFunction() // reset fibonacci function
	s = make([]int, 3, 5)
	s[0] = fi()
	s[1] = fi()
	s[2] = fi()
	// s[3] = fi() // index out of range [3] with length 3
	fmt.Printf("The new fibonacci SLICE is made: %v. length: %v; capacity: %v\n", s, len(s), cap(s))
	s1 := append(s, fi())
	fmt.Printf("\tAppend 1 value to the slice: %v. length: %v; capacity: %v\n", s1, len(s1), cap(s1))
	s2 := append(s1, fi())
	fmt.Printf("\tAppend 1 value to the slice: %v. length: %v; capacity: %v\n", s2, len(s2), cap(s2))
	s3 := append(s2, fi())
	fmt.Printf("\tAppend 1 value to the slice: %v. length: %v; capacity: %v\n", s3, len(s3), cap(s3))
	s4 := append(s3, fi())
	fmt.Printf("\tAppend 1 value to the slice: %v. length: %v; capacity: %v\n", s4, len(s4), cap(s4))
	fmt.Printf("\tThe original fibonacci slice is %v. length: %v; capacity: %v\n", fibonacci, len(fibonacci), cap(fibonacci))

	// Reuse and renew the underlaying array
	// https://blog.golang.org/slices-intro
	fi = GetFibonacciFunction() // reset fibonacci function
	fiArray := [5]int{}
	fiArray[0] = fi()
	fiArray[1] = fi()
	fiArray[2] = fi()
	fmt.Printf("Reset a fibonacci ARRAY: %v. length: %v; capacity: %v\n", fiArray, len(fiArray), cap(fiArray))
	s1 = fiArray[0:3]
	fmt.Printf("\t0:3 slice: %v. length: %v; capacity: %v\n", s1, len(s1), cap(s1))
	s2 = append(s1, fi())
	fmt.Printf("\tAppend 1 value to the 0:3 slice: %v. length: %v; capacity: %v\n", s2, len(s2), cap(s2))
	fmt.Printf("\t\tThe original fibonacci ARRAY updated: %v. length: %v; capacity: %v\n", fiArray, len(fiArray), cap(fiArray))
	s3 = append(s2, fi(), fi(), fi()) // Growing slices (the copy and append functions)
	fmt.Printf("\tAppend 3 values to the slice: %v. length: %v; capacity: %v\n", s3, len(s3), cap(s3))
	fmt.Printf("\t\tThe slice grows beyond capacity. The original fibonacci ARRAY keeps no change.: %v. length: %v; capacity: %v\n", fiArray, len(fiArray), cap(fiArray))

	// Copy
	var sDest = make([]int, 5)
	var n int
	fmt.Printf("Copy: declared a slice destination:  %v. length: %v; capacity: %v\n", sDest, len(sDest), cap(sDest))
	n = copy(sDest, fibonacci[:3])
	fmt.Printf("\t'n = copy(sDest, fibonacci[:3])': n:%v; sDest:%v\n", n, sDest)
	n = copy(sDest, fibonacci[:6])
	// copied slices have their new underlayer array
	nums := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	var numSlice1, numSlice2 = make([]int, 5), make([]int, 8)
	fmt.Printf("Copy: copied slices have their new underlayer array:  %v. length: %v; capacity: %v\n", nums, len(nums), cap(nums))
	copy(numSlice1, nums[:6])
	fmt.Printf("\t'copy(numSlice1, nums[:6])': numSlice1:%v\n", numSlice1)
	copy(numSlice2, nums[3:8])
	fmt.Printf("\t'copy(numSlice2, nums[3:8])': numSlice2:%v\n", numSlice2)
	nums[4] = 99
	fmt.Printf("\t Updated nums[4] = 99. numSlice1:%v; numSlice2:%v\n", numSlice1, numSlice2)
}

// Struct type
type corrdinate struct {
	long int
	lat  int
}

type person struct {
	name string
	age  int
}

type home struct {
	person
	corrdinate
}

func structTypes() {
	// https://golang.org/ref/spec#Struct_types
	location1 := corrdinate{long: 10, lat: 20}
	location2 := corrdinate{90, 80}

	alice := person{name: "Alice", age: 5}
	bob := person{"Bob", 10}

	aliceHome := home{person: alice, corrdinate: location1}
	bobHome := home{bob, location2}
	var unknownHome home

	fmt.Printf("Struct:\n\t%v\n\t%v\n", aliceHome, bobHome)
	fmt.Printf("\tUninitialized struct:%v\n", unknownHome)

	fmt.Printf("\t%v is %v years older than %v\n", bob.name, bob.age-alice.age, alice.name)
}

// Pointer type
func renameByVar(name string) {
	name = name + "Renamed"
}

func renameByPointer(ptr *string) {
	*ptr = *ptr + "Renamed"
}

func pointerTypes() {
	// https://golang.org/ref/spec#Pointer_types
	// https://gobyexample.com/pointers
	alice := "Alice"
	bob := "Bob"

	alicePtr := &alice
	var bobPtr *string = &bob
	var onePtr *string // nil

	fmt.Printf("Pointers initialized:\n")
	fmt.Printf("\talice: %v\tpointer: %v;\t*pointer: %v\n", alice, alicePtr, *alicePtr)
	fmt.Printf("\tbob: %v\tpointer: %v;\t*pointer: %v\n", bob, bobPtr, *bobPtr)
	fmt.Printf("\tUninitialized: pointer: %v\n", onePtr)

	fmt.Printf("Pointers / values changing:\n")
	renameByVar(alice)
	renameByPointer(bobPtr)
	fmt.Printf("\tAlice renamed through var; Bob renamed through pointer\n")
	fmt.Printf("\talice: %v\tpointer: %v;\t*pointer: %v\n", alice, alicePtr, *alicePtr)
	fmt.Printf("\tbob: %v\tpointer: %v;\t*pointer: %v\n", bob, bobPtr, *bobPtr)

	fmt.Printf("Pointers of pointers 'pointerPtr = &bobPtr'\n")
	pointerPtr := &bobPtr
	fmt.Printf("\tAlice's pointer: %v", alicePtr)
	fmt.Printf("\tBob's pointer: %v", bobPtr)
	fmt.Printf("\tThe pointer's pointer (pointerPtr): %v\n", pointerPtr)
	fmt.Printf("'*pointerPtr = alicePtr' Bob gets lost!!\n")
	*pointerPtr = alicePtr
	fmt.Printf("\talicePtr: %v\t*alictPtr: %v\n", alicePtr, *alicePtr)
	fmt.Printf("\tbobPtr: %v\t*bobPtr: %v\n", bobPtr, *bobPtr)
	fmt.Printf("\tpointerPtr: %v\t*pointerPtr: %v;\t**pointerPtr: %v\n", pointerPtr, *pointerPtr, **pointerPtr)
}

// Function Types

func functionTypes() {
	// https://golang.org/ref/spec#Function_types

	fmt.Printf("Functions produce:\n")

	plus := 0

	plusOne := func() {
		plus++
	}
	plusOne()
	fmt.Printf("\tNo return value: 'plusOne()' plus = %v\n", plus)

	plusOneIgnoreInt := func(int) {
		plus++
	}
	plusOneIgnoreInt(3)
	fmt.Printf("\tUnreachable parameter: 'plusOneIgnoreInt(3)' plus = %v\n", plus)

	plusN := func(n int) int {
		plus += n
		return plus
	}
	fmt.Printf("\t'plusN(2)' = %v\n", plusN(2))

	minus := func(a, b int) int {
		return a - b
	}
	fmt.Printf("\t'minus(5, 3)' = %v\n", minus(5, 3))

	divmod := func(a, b int) (int, int) {
		return a / b, a % b
	}
	fmt.Printf("\tReturn multi value: 'divmod(11, 5)' = %v\n", fmt.Sprint(divmod(11, 5)))

	pow := func(a, b int) float64 {
		return math.Pow(float64(a), float64(b))
	}
	fmt.Printf("\t'power(2, 10)' = %v\n", pow(2, 10))

	square := func(a, _ int) float64 {
		return pow(a, 2)
	}
	fmt.Printf("\t'square(2, 10)' = %v\n", square(2, 10))

	sum := func(nums ...int) int {
		// https://gobyexample.com/variadic-functions
		rst := 0
		for _, n := range nums {
			rst += n
		}
		return rst
	}
	fmt.Printf("\tVariadic function: 'sum(1,2,3)' = %v\n", sum(1, 2, 3))
	fmt.Printf("\tVariadic function: 'sum([]int{1, 2, 3, 4, 5}...)' = %v\n", sum([]int{1, 2, 3, 4, 5}...))
}
