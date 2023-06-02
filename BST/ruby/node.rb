class Node 
    @value
    @left
    @right

    def initialize(value)
        @value = value
    end

    def add(value)
        if value < @value
            if @left.nil?
               @left = Node.new(value)
               return true
            end
            return @left.add(value) 
        end
        if value > @value
            if @right.nil?
                @right = Node.new(value)
                return true
            end
            return @right.add(value)
        end
    end

    def contain(value)
        if value < @value
            if @left.nil?
               return false
            end
            return @left.contain(value) 
        end
        if value > @value
            if @right.nil?
                return false
            end
            return @right.contain(value)
        end
        return true
    end

    def length()
        a = @left.nil? ? 0 : @left.length()
        b = @right.nil? ? 0 : @right.length()
        return a + b + 1

    end

    def height()
        
        a = @left.nil? ? 1 : @left.height() + 1
        b = @right.nil? ? 1 : @right.height() + 1
        return a>b ? a : b
    end

end
