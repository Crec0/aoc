package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "strconv"
    s "strings"
)

var printf = fmt.Printf
var parseInt = strconv.Atoi

type inputEntry struct {
    command string
    units   int
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func read_data(path string) []inputEntry {
    file, err := os.Open(path)
    check(err)

    defer file.Close()

    scanner := bufio.NewScanner(file)
    dat := make([]inputEntry, 0)

    for scanner.Scan() {
        line := scanner.Text()
        arr := s.Split(line, " ")

        command, units := arr[0], arr[1]
        parsedInt, err := parseInt(units)
        check(err)

        dat = append(dat, inputEntry{command: command, units: parsedInt})
    }

    return dat
}

func solve_1(data []inputEntry) int {
    h_pos, depth := 0, 0

    for _, entry := range data {
        switch entry.command {

        case "forward":
            h_pos += entry.units

        case "down":
            depth += entry.units

        case "up":
            depth -= entry.units

        }
    }
    return h_pos * depth
}

func solve_2(data []inputEntry) int {

    h_pos, depth, aim := 0, 0, 0

    for _, entry := range data {
        switch entry.command {

        case "forward":
            h_pos += entry.units
            depth += aim * entry.units

        case "down":
            aim += entry.units

        case "up":
            aim -= entry.units
        }
    }
    return h_pos * depth
}

func main() {
    // absPath, err := filepath.Abs("./data/day2/input_example.txt")
    absPath, err := filepath.Abs("./data/day2/input.txt")
    check(err)

    data := read_data(absPath)

    ans_1 := solve_1(data)
    printf("ans 1: %d \n", ans_1)

    ans_2 := solve_2(data)
    printf("ans 2: %d \n", ans_2)
}
