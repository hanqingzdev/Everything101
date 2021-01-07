Following tutorial from https://golang.org/doc/tutorial/getting-started

### Hello World
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

