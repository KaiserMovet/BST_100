require "tree"

function read_numbers_from_file(file_name)
    local numbers = {}
    local file = io.open(file_name, "r")
    if file then
        for line in file:lines() do
            local number = tonumber(line)
            if number then
                table.insert(numbers, number)
            end
        end
        file:close()
    end
    return numbers
end

function get_avg(values)
    local sum = 0
    for _, value in ipairs(values) do
        sum = sum + value
    end
    return sum / #values
end

function main ()
    local add_results = {}
    local check_results = {}
    local len_results = {}
    local height_results = {}

    local add_numbers = read_numbers_from_file("/datasets/add.txt")
    local check_numbers = read_numbers_from_file("/datasets/check.txt")

    for i=1,3 do
        local tree = Tree.new()
        local start_time, end_time
        -- Add elements
        start_time = os.clock()
        for _, value in ipairs(add_numbers) do
            tree:add(value)
        end
        end_time = os.clock()
        add_results[i] = end_time - start_time

        -- Len elements
        start_time = os.clock()
        local length = tree:length()
        end_time = os.clock()
        len_results[i] = end_time - start_time
        print("Length=" .. length)

        -- height elements
        start_time = os.clock()
        local height = tree:height()
        end_time = os.clock()
        height_results[i] = end_time - start_time
        print("Height=" .. height)

        -- Check elements
        start_time = os.clock()
        for _, value in ipairs(check_numbers) do
            tree:contain(value)
        end
        end_time = os.clock()
        check_results[i] = end_time - start_time

    end

    print("Average add:".. string.format("%.2f",get_avg(add_results)))
    print("Average check:".. string.format("%.2f",get_avg(check_results)))
    print("Average len:".. string.format("%.2f",get_avg(len_results)))
    print("Average height:".. string.format("%.2f",get_avg(height_results)))

end
main()