mod day1;
mod day2;
mod day3;
mod day4;

fn main() {
    let contents = std::fs::read_to_string("./src/day4/data.txt").expect("Read the file");
    day4::day4::solve(&contents);
}
