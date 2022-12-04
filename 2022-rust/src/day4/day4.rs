fn parse_range(string: &str) -> (u32, u32) {
    let split = string.split("-").collect::<Vec<&str>>();
    let (left, right) = (split[0], split[1]);
    return (
        u32::from_str_radix(left, 10).unwrap(),
        u32::from_str_radix(right, 10).unwrap(),
    );
}

#[allow(dead_code)]
pub fn solve(contents: &str) {
    let complete_overlaps = contents
        .lines()
        .map(|line| line.split(",").collect::<Vec<_>>())
        .filter(|split| {
            let (left, right) = (parse_range(split[0]), parse_range(split[1]));
            (left.0 <= right.0 && left.1 >= right.1) || (left.0 >= right.0 && left.1 <= right.1)
        })
        .count();

    println!("Solution 1: {:?}", complete_overlaps);

    let partial_overlaps = contents
        .lines()
        .map(|line| line.split(",").collect::<Vec<_>>())
        .filter(|split| {
            let (left, right) = (parse_range(split[0]), parse_range(split[1]));
            (left.0 <= right.0 && left.1 >= right.1)
                || (left.0 >= right.0 && left.1 <= right.1)
                || (left.1 >= right.0) && (right.1 >= left.0)
        })
        .count();

    println!("Solution 2: {:?}", partial_overlaps);
}
