pub struct Node{
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Node{
    pub fn new(value: i32) -> Node {
        Node {value: value, left: None, right: None}
    }
}

impl Node{
    pub fn add(&mut self, value: i32) -> bool {
        if value < self.value {
            match self.left.as_mut() {
                None => {self.left = Some(Box::new(Node::new(value))); return false},
                Some(left) => return left.add(value),
            }
        }

        if value > self.value {
            match self.right.as_mut() {
                None => {self.right = Some(Box::new(Node::new(value))); return false},
                Some(right) => return right.add(value),
            }
        }

        return false
    
    }

    pub fn contain(&mut self, value: i32) -> bool{
        if value < self.value {
            match self.left.as_mut() {
                None => {return false},
                Some(left) => return left.contain(value),
            }
        }

        if value > self.value {
            match self.right.as_mut() {
                None => { return false},
                Some(right) => return right.contain(value),
            }
        }

        return false
    
    }

    pub fn length(&mut self)->i32{
        let mut left_len: i32 = 0;
        match self.left.as_mut() {
            None =>{},
            Some(node) => {left_len = node.length()}, 
        }

        let mut right_len: i32 = 0;
        match self.right.as_mut() {
            None =>{},
            Some(node) => {right_len = node.length()}, 
        }

        return left_len + right_len + 1;
    }

    pub fn height(&mut self)->i32{
        let mut left_height: i32 = 0;
        match self.left.as_mut() {
            None =>{},
            Some(node) => {left_height = node.height()}, 
        }

        let mut right_height: i32 = 0;
        match self.right.as_mut() {
            None =>{},
            Some(node) => {right_height = node.height()}, 
        }
        if left_height > right_height {return left_height + 1}
        return right_height + 1;
    }
}
