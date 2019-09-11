
from flask import Flask, render_template


class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []
        #genesis block
        self.create_block(0,'00')

    def create_block(self, nonce, previous_hash):
        block = {
            'block number' : len(self.chain)+1,
            'transactions' : self.transactions,
            'nonce': nonce,
            'previous_hash' : previous_hash
        }
        # Reset current list of transaction
        self.transactions = []
        self.chain.append(block)



# Instantiate the Blockchain
blockchain = Blockchain()

# Instantiate the Node
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port
    app.run(host='127.0.0.1', port=port, debug=True)