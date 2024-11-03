from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Predefined lists of products based on waste type
waste_products = {
    "plastic": [
        "Recycled plastic bricks for construction",
        "Plastic lumber for outdoor furniture",
        "Insulating materials for buildings",
        "Eco-friendly tote bags",
        "Decorative tiles for interiors"
    ],
    "glass": [
        "Recycled glass countertops",
        "Glass tiles for decoration",
        "Fiberglass insulation",
        "Glass bottles and jars",
        "Glass beads for sandblasting"
    ],
    "metal": [
        "Recycled metal cans",
        "Construction steel beams",
        "Metal art and sculptures",
        "Automobile parts",
        "Electronic components"
    ],
    "paper": [
        "Recycled paper notebooks",
        "Cardboard packaging",
        "Paper pulp for insulation",
        "Eco-friendly gift wrapping",
        "Compostable seed pots"
    ]
    # Add more waste types as needed
}

@app.route('/generate-products', methods=['POST'])
def generate_products():
    data = request.json
    waste_type = data.get('waste_type', '').lower()

    # Fetch product suggestions based on waste type
    products = waste_products.get(waste_type)

    if products:
        return jsonify({'products': products})
    else:
        return jsonify({'error': 'No valid waste type provided or no products available for this type.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
