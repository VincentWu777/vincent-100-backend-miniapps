"""
1. Command Processor
    Function name: command_processor(input_str)
    Input: string
    Output: (command_type, payload)
        command_type ∈ {"quit", "history", "expression"}
        payload: None or expression string

2. Expression Evaluator
    Function name: expression_evaluator(expr)
    Input: string
    Output: (success, value)
        success: boolean
        value: result number or error message string

3. History Manager
    (a) add_history(history_list, expr, result)
        Input: list, string, any
        Output: None (modify list in place)

    (b) print_history(history_list)
        Input: list
        Output: None (prints to terminal)

4. Main Loop
    Function name: main_loop()
    Responsibilities:
        - Read user input
        - Identify command type
        - Handle quit
        - Handle history display
        - Evaluate expressions
        - Update history
        - Print results
"""
def command_processor(input_str):
    clean = input_str.strip().lower()
    if clean in ("quit", "history"):
        return clean, None
    else:
        return "expression", input_str

def expression_evaluator(expr):
    try:
        result = eval(expr)
        return True, result
    except Exception as e:
        return False, f'Error: {e}'

def add_history(history_list, expr, result):
    history_list.append((expr, result))

def print_history(history_list):
    if not history_list:
        print("No history yet.")
        return

    for idx, (expr, result) in enumerate(history_list, start=1):
        print(f'{idx}: {expr} = {result}')

def main_loop():
    history_list = []
    while True:
        input_str = input("> ")
        cmd_type, payload = command_processor(input_str)
        if cmd_type == "quit":
            print("Goodbye!")
            break
        if cmd_type == "history":
            print_history(history_list)
            continue
        if cmd_type == "expression":
            success, result = expression_evaluator(payload)
            if success:
                print(f'= {result}')
                add_history(history_list, payload, result)
            else:
                print(result)

if __name__ == "__main__":
    main_loop()




