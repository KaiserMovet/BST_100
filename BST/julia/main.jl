# main.jl

using DelimitedFiles
include("tree.jl")

function get_numbers(path::String)::Vector{Int}
    content = read(path, String)
    numbers = [parse(Int, i) for i in split(content)]
    return numbers
end

function main()
    amount = parse(Int, ARGS[1])

    add_numbers = get_numbers("/datasets/add.txt")[1:amount]
    check_numbers = get_numbers("/datasets/check.txt")[1:amount]

    bst = Tree(nothing)

    # Add elements
    start_time = time()
    for i in add_numbers
        add(bst, i)
    end
    end_time = time()
    println("ADD_TEST: ", end_time - start_time)

    # Check elements
    start_time = time()
    for i in check_numbers
        contain(bst, i)
    end
    end_time = time()
    println("CHECK_TEST: ", end_time - start_time)

    # Len elements
    start_time = time()
    for _ in 1:10
        length(bst)
    end
    end_time = time()
    println("LEN_TEST: ", (end_time - start_time)/10)

    # Height elements
    start_time = time()
    for _ in 1:10
        height(bst)
    end
    end_time = time()
    println("HEIGHT_TEST: ", (end_time - start_time)/10)

    println("VALIDATION: ", length(bst), ":", height(bst))
end

main()
