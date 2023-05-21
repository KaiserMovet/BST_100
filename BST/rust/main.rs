use std::fs::File;
use std::io::Read;
use std::time::Instant;
use std::env;

mod bst;

fn get_numbers_from_file(filename: &str) -> Vec<i32> {
    let mut file = File::open(filename).expect("Failed to open file");
    let mut content = String::new();
    file.read_to_string(&mut content).expect("Failed to read file");
    let numbers: Vec<i32> = content.split_whitespace()
        .map(|s| s.parse().expect("Failed to parse number"))
        .collect();
    numbers
}

fn get_add_numbers() -> Vec<i32> {
    return get_numbers_from_file("/datasets/add.txt");
}

fn get_check_numbers() -> Vec<i32> {
    return get_numbers_from_file("/datasets/check.txt");

}

fn main() {

    let amount: i32 = env::args().nth(1).unwrap().parse().expect("Integer is expected");

    let add_numbers: Vec<i32> = get_add_numbers().iter().take(amount as usize).cloned().collect();
    let check_numbers: Vec<i32> = get_check_numbers().iter().take(amount as usize).cloned().collect();


    let mut tree = bst::tree::Tree::new();
    
    // Add elements
    let start_time = Instant::now();
    for &i in &add_numbers {
        tree.add(i);
    }
    let end_time = Instant::now();
    println!("ADD_TEST:{}", (end_time - start_time).as_secs_f64());

    // Check elements
    let start_time = Instant::now();
    for &i in &check_numbers {
        tree.contain(i);
    }
    let end_time = Instant::now();
    println!("CHECK_TEST:{}", (end_time - start_time).as_secs_f64());
    
    // Len elements
    let start_time = Instant::now();
    for _ in 0..10 {
        tree.length();
    }
    let end_time = Instant::now();
    println!("LEN_TEST:{}", (end_time - start_time).as_secs_f64()/10.0);

    // Height elements
    let start_time = Instant::now();
    for _ in 0..10 {
        tree.height();
    }
    let end_time = Instant::now();
    println!("HEIGHT_TEST:{}", (end_time - start_time).as_secs_f64()/10.0);

    println!("VALIDATION:{}:{}", tree.length(), tree.height());

}
