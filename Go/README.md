## Hello World
Directories: `greetings/`, `hello/`
Following tutorial from https://golang.org/doc/tutorial/getting-started

### The 1st Hello World
- https://golang.org/doc/tutorial/getting-started#code
```shell
cd hello
go run hello.go
```

### Call code in an external package
- https://golang.org/doc/tutorial/getting-started#call
```shell
go mod init hello
go run hello.go
```

### Create a Go Module
- https://golang.org/doc/tutorial/create-module
```shell
go build
./hello
```

### Error handling
- https://golang.org/doc/tutorial/handle-errors
```shell
go run hello.go
```

### Random
- https://golang.org/doc/tutorial/random-greeting

*Note: The shell command is [fish-shell](https://fishshell.com/) style.*

```shell
go build
for i in (seq 1 5); ./hello; end
```
### Passing a slice: Map, for, range
- https://golang.org/doc/tutorial/greetings-multiple-people
```shell
go run hello.go
```

### Unit testing
- https://golang.org/doc/tutorial/add-a-test
```shell
cd ../greetings/
go test
go test -v
```

### Compile and install
- https://golang.org/doc/tutorial/compile-install
```shell
cd ../hello
go list -f '{{.Target}}'
go install
hello
```
## 101 Hello World
```shell
go run hello101.go
```
