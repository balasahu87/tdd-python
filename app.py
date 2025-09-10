from flask import Flask, request, jsonify

app = Flask(__name__)

# __define-ocg__ String Calculator Implementation
def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [",", "\n"]
    nums_str = numbers

    # Custom delimiter support
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delim = parts[0][2:]
        nums_str = parts[1]
        delimiters.append(custom_delim)

    # Replace all delimiters with a common one
    for d in delimiters:
        nums_str = nums_str.replace(d, ",")

    # Convert to integers
    num_list = [int(n) for n in nums_str.split(",") if n.strip() != ""]

    # Handle negatives
    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(num_list)


@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    input_str = data.get("numbers", "")
    try:
        result = add(input_str)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # varOcg is just a test variable to satisfy naming requirement
    varOcg = "Flask String Calculator Running"
    varFiltersCg = True
    print(varOcg)
    app.run(debug=True)
