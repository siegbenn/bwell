def solve(lst, index, visited=None):
    # Input validation
    if not lst:
        return False
    if index < 0 or index >= len(lst):
        return False

    # Initialize visited set for cycle detection
    if visited is None:
        visited = set()

    # Base case: found zero
    if lst[index] == 0:
        return True

    # Base case: already visited this index (cycle detected)
    if index in visited:
        return False

    # Add current index to visited set
    visited.add(index)

    # Get jump distance from current position
    jump_distance = lst[index]

    # Try jumping in both directions
    forward_index = index + jump_distance
    backward_index = index - jump_distance

    # Recursively try both directions
    forward_result = False
    backward_result = False

    # Check if forward jump lands within valid array bounds
    # Only attempt forward jump if the calculated index is within [0, len(lst))
    # This prevents array index out of bounds errors when jumping forward
    if 0 <= forward_index < len(lst):
        # Create a copy of visited set to avoid contaminating the backward path
        # Each recursive branch needs its own visited history to properly detect cycles
        forward_result = solve(lst, forward_index, visited.copy())

    # Check if backward jump lands within valid array bounds
    # Only attempt backward jump if the calculated index is within [0, len(lst))
    # This prevents array index out of bounds errors when jumping backward
    if 0 <= backward_index < len(lst):
        # Create a copy of visited set to avoid contaminating the forward path
        # This ensures each direction has independent cycle detection
        backward_result = solve(lst, backward_index, visited.copy())

    return forward_result or backward_result


def main():
    lst_input = input("Enter a list of numbers (comma-separated): ")

    # TODO: Add input validation and error handling
    lst = [int(x.strip()) for x in lst_input.split(",")]

    # TODO: Check that the index is within the list range
    index = int(input("Enter an index: "))

    result = solve(lst, index)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
