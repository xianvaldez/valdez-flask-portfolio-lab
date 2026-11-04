from flask import Flask, render_template, request, redirect, url_for, jsonify

from linked_list import LinkedList
from stack import Stack
from queue_deque import Queue, Deque
from infix_to_postfix import infix_to_postfix

from sorting_algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

from area_calculators import area_of_circle, area_of_triangle
from string_operations import convert_to_uppercase


app = Flask(__name__)

linked_list = LinkedList()
stack = Stack()
queue = Queue()
deque_list = Deque()


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
        result = convert_to_uppercase(input_string)

    return render_template('works.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None

    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', ''))
            if radius < 0:
                raise ValueError
            result = area_of_circle(radius)
        except ValueError:
            result = "Invalid radius."

    return render_template('circle.html', result=result)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None

    if request.method == 'POST':
        try:
            base = float(request.form.get('base', ''))
            height = float(request.form.get('height', ''))

            if base < 0 or height < 0:
                raise ValueError

            result = area_of_triangle(base, height)

        except ValueError:
            result = "Invalid base or height."

    return render_template('triangle.html', result=result)


@app.route('/works/linked-list')
def linked_list_page():
    return render_template(
        'linked_list.html',
        values=linked_list.to_list()
    )


@app.route('/works/linked-list/insert', methods=['POST'])
def linked_list_insert():
    data = request.form.get('data', '').strip()
    position = request.form.get('position', 'end')

    if not data:
        return jsonify({
            'success': False,
            'message': 'Please enter a node value.'
        })

    if position == 'beginning':
        linked_list.insert_at_beginning(data)
    elif position == 'end':
        linked_list.insert_at_end(data)
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid insertion position.'
        })

    return jsonify({
        'success': True,
        'values': linked_list.to_list()
    })


@app.route('/works/linked-list/clear', methods=['POST'])
def linked_list_clear():
    linked_list.clear()

    return jsonify({
        'success': True,
        'values': linked_list.to_list()
    })


@app.route('/works/stack')
def stack_page():
    return render_template(
        'stack.html',
        values=stack.to_list(),
        top=stack.peek()
    )


@app.route('/works/stack/push', methods=['POST'])
def stack_push():
    data = request.form.get('data', '').strip()

    if data:
        stack.push(data)

    return redirect(url_for('stack_page'))


@app.route('/works/stack/pop', methods=['POST'])
def stack_pop():
    stack.pop()
    return redirect(url_for('stack_page'))


@app.route('/works/infix-to-postfix', methods=['GET', 'POST'])
def infix_postfix_page():
    expression = ''
    result = None
    error = None

    if request.method == 'POST':
        expression = request.form.get('expression', '').strip()

        if expression:
            try:
                result = infix_to_postfix(expression)
            except ValueError as e:
                error = str(e)
        else:
            error = "Please enter an expression."

    return render_template(
        'infix_postfix.html',
        expression=expression,
        result=result,
        error=error
    )


# Queue and Deque
@app.route('/works/queue-deque')
def queue_deque_page():
    return render_template(
        'queue_deque.html',
        queue_values=queue.to_list(),
        queue_front=queue.peek(),
        deque_values=deque_list.to_list()
    )


@app.route('/works/queue/enqueue', methods=['POST'])
def queue_enqueue():
    data = request.form.get('data', '').strip()

    if data:
        queue.enqueue(data)

    return redirect(url_for('queue_deque_page'))


@app.route('/works/queue/dequeue', methods=['POST'])
def queue_dequeue():
    queue.dequeue()
    return redirect(url_for('queue_deque_page'))


@app.route('/works/deque/add-front', methods=['POST'])
def deque_add_front():
    data = request.form.get('data', '').strip()

    if data:
        deque_list.add_front(data)

    return redirect(url_for('queue_deque_page'))


@app.route('/works/deque/add-rear', methods=['POST'])
def deque_add_rear():
    data = request.form.get('data', '').strip()

    if data:
        deque_list.add_rear(data)

    return redirect(url_for('queue_deque_page'))


@app.route('/works/deque/remove-front', methods=['POST'])
def deque_remove_front():
    deque_list.remove_front()
    return redirect(url_for('queue_deque_page'))


@app.route('/works/deque/remove-rear', methods=['POST'])
def deque_remove_rear():
    deque_list.remove_rear()
    return redirect(url_for('queue_deque_page'))


@app.route('/works/sorting', methods=['GET', 'POST'])
def sorting_page():
    result = None
    original = None
    selected_algorithm = ''
    error = None

    algorithms = {
        'bubble': bubble_sort,
        'selection': selection_sort,
        'insertion': insertion_sort,
        'merge': merge_sort,
        'quick': quick_sort
    }

    if request.method == 'POST':
        numbers = request.form.get('numbers', '').strip()
        selected_algorithm = request.form.get('algorithm', '')

        try:
            original = [int(x.strip()) for x in numbers.split(',')]

            if selected_algorithm not in algorithms:
                error = "Please select a sorting algorithm."
                original = None
            else:
                result = algorithms[selected_algorithm](original)

        except ValueError:
            error = "Please enter valid numbers separated by commas."

    return render_template(
        'sorting.html',
        result=result,
        original=original,
        selected_algorithm=selected_algorithm,
        error=error
    )


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
