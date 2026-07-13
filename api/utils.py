def from_base58_num(b58_str: str) -> int:
    """Decodes a compact Base58 positional number back to a standard integer."""
    # Omitted O and 0
    # Omitted l and I 
    # No special chars .
    chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    print(len(chars))
    
    # Map each character to its index/value
    char_to_val = {char: idx for idx, char in enumerate(chars)}
    
    result = 0
    for char in b58_str:
        result = (result * 58) + char_to_val[char]
        
    return result