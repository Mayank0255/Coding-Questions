def order_weight(strng):
    weights = sorted(strng.split(" "))
    sorted_weights = sorted(weights, key=digit_sumV2);
    return " ".join(sorted_weights)

def digit_sumV2(a_string):
    return sum( [int(char) for char in a_string] )
