mutable struct Node
    value::Int 
    left::Union{Node, Nothing}
    right::Union{Node, Nothing}
end

function add(self::Node, value::Int)
    if value < self.value
        if isnothing(self.left)
            self.left = Node(value, nothing, nothing)
            return true
        end
        return add(self.left, value)
    elseif value > self.value
        if isnothing(self.right)
            self.right = Node(value, nothing, nothing)
            return true
        end
        return add(self.right, value)
    end

    return false
end

function contain(self::Node, value::Int)
    if value < self.value
        if isnothing(self.left)
            return false
        end
        return contain(self.left, value)
    elseif value > self.value
        if isnothing(self.right)
            return false
        end
        return contain(self.right, value)
    end

    return true
end

function length(self::Node)
    a = isnothing(self.left) ? 0 : length(self.left)
    b = isnothing(self.right) ? 0 : length(self.right)
    return a + b + 1
end

function height(self::Node)
    a = isnothing(self.left) ? 1 : height(self.left) + 1
    b = isnothing(self.right) ? 1 : height(self.right) + 1
    return max(a, b)
end
