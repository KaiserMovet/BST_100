package main

type Node struct {
	value int
	left *Node
	right *Node
}

func (self *Node) Add(value int) bool {
	if value < self.value {
		if self.left == nil {
			self.left = &Node{value: value, left: nil, right: nil}
			return true
		}
		return self.left.Add(value) 
	}

	if value > self.value {
		if self.right == nil {
			self.right = &Node{value: value, left:nil, right:nil}
			return true
		}
		return self.right.Add(value)
	}
	return false
}

func (self *Node) Contain(value int) bool {
	if value < self.value {
		if self.left == nil {
			return false
		}
		return self.left.Contain(value)
	}

	if value > self.value {
		if self.right == nil {
			return false
		}
		return self.right.Contain(value)
	}
	return true
}

func (self *Node) Length() int {
	a := 0
	if self.left != nil {
		a = self.left.Length()
	}
	b := 0
	if self.right != nil {
		b = self.right.Length()
	}
	return a + b + 1
}

func (self *Node) Height() int {
	a := 1
	if self.left != nil {
		a = self.left.Height() + 1
	}
	b := 1
	if self.right != nil {
		b = self.right.Height() + 1
	}
	if a > b{
		return a
	}
	return b
}