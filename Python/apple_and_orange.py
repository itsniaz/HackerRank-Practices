def main():
    house_range = input()
    h_arr = house_range.split(" ")
    #s
    house_start =  int(h_arr[0])
    #t
    house_end = int(h_arr[1])

    apple_n_orange = input()
    tree_arr = apple_n_orange.split(" ")
    
    #a
    apple_tree = int(tree_arr[0])
    #b
    orange_tree = int(tree_arr[1])

    number_of_fruits_thrown = input()
    number_of_fruits_arr = number_of_fruits_thrown.split(" ")

    #m
    apple_fruit = int(number_of_fruits_arr[0])
    #n
    orange_fruit = int(number_of_fruits_arr[1])

    #apple_thrown
    apple_throw_arr = input().split(" ")
    apple_throw_arr = list(map(int,apple_throw_arr))

    #orange_thrown 
    orange_throw_arr = input().split(" ")
    orange_throw_arr = list(map(int,orange_throw_arr))

    #Here begins the logic
    num_apple_falls = 0
    num_orange_falls = 0

    for apple in apple_throw_arr:
        actual_pos = apple_tree+apple
        if(actual_pos>=house_start and actual_pos<=house_end):
            num_apple_falls += 1
    for orange in orange_throw_arr:
        actual_pos = orange_tree+orange
        if(actual_pos>=house_start and actual_pos<=house_end):
            num_orange_falls += 1
    
    print("{}\n{}".format(num_apple_falls,num_orange_falls))

main()