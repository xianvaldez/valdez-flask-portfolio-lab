from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


linked_list = LinkedList()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('works.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            if radius < 0:
                result = "Radius cannot be negative."
            else:
                result = round(3.14159 * radius * radius, 2)
        except ValueError:
            result = "Please enter a valid number."
    return render_template('circle.html', result=result)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            if base < 0 or height < 0:
                result = "Base and height cannot be negative."
            else:
                result = round(0.5 * base * height, 2)
        except ValueError:
            result = "Please enter valid numbers."
    return render_template('triangle.html', result=result)


@app.route('/works/linked-list')
def linked_list_page():
    return render_template('linked_list.html', values=linked_list.to_list())


@app.route('/works/linked-list/insert', methods=['POST'])
def linked_list_insert():
    data = request.form.get('data', '').strip()
    position = request.form.get('position', 'end')

    if not data:
        return jsonify({"success": False, "message": "Please enter a value."})

    if position == 'beginning':
        linked_list.insert_at_beginning(data)
    else:
        linked_list.insert_at_end(data)

    return jsonify({
        "success": True,
        "values": linked_list.to_list()
    })


@app.route('/works/linked-list/clear', methods=['POST'])
def linked_list_clear():
    linked_list.head = None
    linked_list.tail = None
    return jsonify({"success": True, "values": []})


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
