use std::fs::File;
use std::io::Read;
use std::time::Instant;

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
    let mut x = bst::tree::Tree::new(); 
    x.add(3);

    let mut add_results = Vec::new();
    let mut check_results = Vec::new();
    let mut len_results = Vec::new();
    let mut height_results = Vec::new();

    let add_numbers = get_add_numbers();
    let check_numbers = get_check_numbers();

    for _ in 0..3 {
        let mut tree = bst::tree::Tree::new();
        
        // Add elements
        let start_time = Instant::now();
        for &i in &add_numbers {
            tree.add(i);
        }
        let end_time = Instant::now();
        let add_duration = end_time - start_time;
        add_results.push(add_duration.as_secs_f64());

        // Len elements
        let start_time = Instant::now();
        let length = tree.length();
        let end_time = Instant::now();
        let len_duration = end_time - start_time;
        len_results.push(len_duration.as_secs_f64());
        println!("length: {}", length);

        // Height elements
        let start_time = Instant::now();
        let height = tree.height();
        let end_time = Instant::now();
        let height_duration = end_time - start_time;
        height_results.push(height_duration.as_secs_f64());
        println!("height: {}", height);

        // Check elements
        let start_time = Instant::now();
        for &i in &check_numbers {
            tree.contain(i);
        }
        let end_time = Instant::now();
        let check_duration = end_time - start_time;
        check_results.push(check_duration.as_secs_f64()); 
    }

    let average_add: f64 = add_results.iter().sum::<f64>() / add_results.len() as f64;
    let average_check: f64 = check_results.iter().sum::<f64>() / check_results.len() as f64;
    let average_len: f64 = len_results.iter().sum::<f64>() / len_results.len() as f64;
    let average_height: f64 = height_results.iter().sum::<f64>() / height_results.len() as f64;

    println!("Average add: {:.2}", average_add);
    println!("Average check: {:.2}", average_check);
    println!("Average len: {:.2}", average_len);
    println!("Average height: {:.2}", average_height);
}
