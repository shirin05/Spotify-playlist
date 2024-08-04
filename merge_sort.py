def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] < right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


# test data to verify performance 
hi = ['spotify:track:6X3FZtz4cKU2MKSQlGG9ZG',
 'spotify:track:0jiW3PNiHJxOhWh9oPBJ7m',
 'spotify:track:4XkOcWt0C2JX1s2RXybosk',
 'spotify:track:4ArjAoBnwEKgsA1atl1asm',
 'spotify:track:1P7ycI8RxUZVErR2xCPqbA',
 'spotify:track:4VYmdTVFXDq0LtYMoVswTv',
 'spotify:track:5mexbTuWx9d8DPZk4sDGF4',
 'spotify:track:5ZJABzmKr9flocrtQqbINO',
 'spotify:track:7EHAXZenBzmGCpccWCyg8z',
 'spotify:track:3HXSQWIyz7CUEI96kUurwn',
 'spotify:track:7oopoWQa0jicMSf9SFtxMK',
 'spotify:track:6xXYFVsFDGSLNzeE9zGCiL',
 'spotify:track:6b4A1mLzePAHGn3XCicLAe',
 'spotify:track:2LNMhZ3YijTO7USmqjgJfG',
 'spotify:track:6FhEDaaRFyPRMYqhhXivO9',
 'spotify:track:2NjeQLvFsfeKdZoA7dbfL1',
 'spotify:track:4d8BSdhx6WT5GtTOWpv4rh',
 'spotify:track:5vm7y9SmcH0S1NOQanb8rQ',
 'spotify:track:1MTRFYSerX3m4VxavhihPm',
 'spotify:track:2ENHsB59lQBMnpBUQTWG8T']

print(760//100)