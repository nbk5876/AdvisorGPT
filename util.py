#============================================================
# util.py
# Purpose: Utilies
#============================================================

def reformat_advice(advice_text):
    # Split the advice into lines and remove empty lines
    lines = [line for line in advice_text.split('\n') if line.strip() != '']
    
    # Reformat lines to add a single newline for readability
    reformatted_lines = []
    for line in lines:
        reformatted_lines.append(line)
        # Add a newline after each line for separation
        reformatted_lines.append('\n')
    
    # Join the lines back into a single string, removing the last added newline
    reformatted_text = ''.join(reformatted_lines[:-1])

    return reformatted_text

# Example usage
#unformatted_advice = "Your unformatted advice text here..."
#formatted_advice = reformat_advice(unformatted_advice)
#print(formatted_advice)
