#[allow(dead_code)]
pub fn solve(contents: &str) {
    let mut lines: Vec<i32> = contents
        .split("\n\n")
        .map(|elf| elf.lines().map(|val| val.parse::<i32>().unwrap()).sum())
        .collect();

    println!("Solution 1: {:?}", lines.iter().max().unwrap());

    lines.sort();
    lines.reverse();

    println!("Solution 2: {:?}", lines.iter().take(3).sum::<i32>());
}
