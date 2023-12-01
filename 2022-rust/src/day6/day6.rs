
fn contains_duplicates(string: &str) -> bool {
    let mut chars: Vec<_> = string.chars().collect();
    chars.sort();
    for (idx, elem) in chars.iter().enumerate().skip(1) {
        if elem == &chars[idx - 1] {
            return true;
        }
    }
    return false;
}


fn find_non_repeating_index(contents: &str, distinct: usize) -> u32 {
    for idx in 0..(contents.len() - (distinct - 1)) {
        if !contains_duplicates(&contents[idx..(idx+distinct)]) {
            return (idx + distinct) as u32;
        }
    }
    u32::MAX
}


#[allow(dead_code)]
pub fn solve(contents: &str) {
    let sol1 = find_non_repeating_index(contents, 4);
    println!("Solution 1: {}", sol1);
    let sol1 = find_non_repeating_index(contents, 14);
    println!("Solution 2: {}", sol1);
}
