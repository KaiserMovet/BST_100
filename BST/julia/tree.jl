include("node.jl")

mutable struct Tree
    root::Union{Node, Nothing}
end

function add(self::Tree,value::Int)
    if isnothing(self.root)
        self.root = Node(value, nothing, nothing)
        return true
    end
    return add(self.root, value)
end

function contain(self::Tree,value::Int)
    if isnothing(self.root)
        return false
    end
    return contain(self.root, value)
end

function length(self::Tree)
    if isnothing(self.root)
        return 0
    end
    return length(self.root)
end
function height(self::Tree)
    if isnothing(self.root)
        return 0
    end
    return height(self.root)
end

