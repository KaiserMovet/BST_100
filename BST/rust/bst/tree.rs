use crate::bst::node::Node;

pub struct Tree{
    root: Option<Box<Node>>,
}

impl Tree{
    pub fn new() -> Tree {
        Tree { root: None::<Box<Node>> }
    }
}

impl Tree{
    pub fn add(&mut self, value: i32) -> bool{
        match self.root.as_mut() {
            None =>{self.root = Some(Box::new(Node::new(value))); return true},
            Some(node) => {return node.add(value)}, 
        }
    }

    pub fn contain(&mut self, value: i32) -> bool{
        match self.root.as_mut() {
            None =>{return false},
            Some(node) => {return node.contain(value)}, 
        }
    }

    pub fn length(&mut self)->i32{
        match self.root.as_mut() {
            None =>{return 0},
            Some(node) => {return node.length()}, 
        }
    }

    pub fn height(&mut self)->i32{
        match self.root.as_mut() {
            None =>{return 0},
            Some(node) => {return node.height()}, 
        }
    }
}