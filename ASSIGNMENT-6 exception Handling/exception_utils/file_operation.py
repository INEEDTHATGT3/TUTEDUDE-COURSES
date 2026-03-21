def read_safe(filename, lines=3):
    try: 
        with open(filename, 'r') as f:
            content = [f.readline().strip() for _ in range(lines)]
            return [line for line in content if line]
    except FileNotFoundError:
        raise FileNotFoundError(f"System Error: '{filename}' not found.")
    except PermissionError:
        raise PermissionError(f"System Error: Access denied for '{filename}'.")