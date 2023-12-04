package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// Partnum represents a structure to store number and points
type Partnum struct {
	number string
	points []point
	isPart bool
}

type point struct {
	row, col int
}

func (p *Partnum) addDigit(val string, row, col int) {
	p.number += val
	p.points = append(p.points, point{row, col})
}

func getAdjacentPoints(row, col int, rows, cols int) []point {
	points := []point{}

	directions := [8][2]int{
		{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {-1, -1}, {0, -1},
	}

	for _, vector := range directions {
		tmpRow, tmpCol := row+vector[0], col+vector[1]

		if tmpRow < 0 || tmpRow >= rows || tmpCol < 0 || tmpCol >= cols {
			continue
		}

		points = append(points, point{tmpRow, tmpCol})
	}

	return points
}

func isSymbol(char string) bool {
	if _, err := strconv.Atoi(char); err == nil {
		return false
	}
	if char == "." {
		return false
	}
	return true
}

// isEqual checks if two Partnum structs are equal
func isEqual(a, b Partnum) bool {
	if a.number != b.number || a.isPart != b.isPart || len(a.points) != len(b.points) {
		return false
	}
	for i := range a.points {
		if a.points[i] != b.points[i] {
			return false
		}
	}
	return true
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <input_file>")
		return
	}

	inputFile := os.Args[1]

	file, err := os.Open(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var data [][]string

	for scanner.Scan() {
		line := scanner.Text()
		row := []string{}
		for _, char := range line {
			row = append(row, string(char))
		}
		data = append(data, row)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	rows, cols := len(data), len(data[0])

	fmt.Println("data", data)
	fmt.Println("shape", rows, cols)
	fmt.Println("corners", data[0][0], data[rows-1][cols-1])

	parts := []Partnum{}
	part := Partnum{}

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			current := point{r, c}

			if _, err := strconv.Atoi(data[current.row][current.col]); err == nil {
				part.addDigit(data[current.row][current.col], current.row, current.col)
				adjPoints := getAdjacentPoints(current.row, current.col, rows, cols)
				for _, x := range adjPoints {
					if isSymbol(data[x.row][x.col]) {
						part.isPart = true
						break
					}
				}
				continue
			}

			if !isSymbol(data[current.row][current.col]) && part.number != "" {
				if part.isPart {
					parts = append(parts, part)
				}
				part = Partnum{}
			}
		}

		if part.number != "" {
			if part.isPart {
				parts = append(parts, part)
			}
			part = Partnum{}
		}
	}

	sumParts := 0
	for _, x := range parts {
		num, _ := strconv.Atoi(x.number)
		sumParts += num
	}

	fmt.Println("ans part1", sumParts)
	fmt.Println(parts)

	ans := 0

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			current := point{r, c}

			if data[current.row][current.col] == "*" {
				gearParts := []Partnum{}

				adjPoints := getAdjacentPoints(current.row, current.col, rows, cols)
				for _, point := range adjPoints {
					for _, part := range parts {
						for _, p := range part.points {
							if point == p {
								gearParts = append(gearParts, part)
							}
						}
					}
				}

				uniqueGearParts := []Partnum{}
				for _, part := range gearParts {
					found := false
					for _, uniquePart := range uniqueGearParts {
						if isEqual(part, uniquePart) {
							found = true
							break
						}
					}
					if !found {
						uniqueGearParts = append(uniqueGearParts, part)
					}
				}g

				if len(uniqueGearParts) == 2 {
					num1, _ := strconv.Atoi(uniqueGearParts[0].number)
					num2, _ := strconv.Atoi(uniqueGearParts[1].number)
					ans += num1 * num2
				}

				fmt.Println(current, uniqueGearParts)
			}
		}
	}

	fmt.Println("ans part2", ans)
}
