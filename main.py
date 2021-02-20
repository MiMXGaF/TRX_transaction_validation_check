import requests
import datetime


def check_transaction(tx):
    time = requests.get("http://worldtimeapi.org/api/timezone/Europe/London")
    time = time.json()
    time = int(time['unixtime'])
    transaction = requests.get(f'https://apilist.tronscan.org/api/transaction-info?hash={tx}')
    transaction = transaction.json()
    if transaction == {}:
        print('transaction not found!')
    else:
        hash = transaction['hash']
        size = len(str(transaction['timestamp']))
        timestamp = str(transaction['timestamp'])
        timestamp = timestamp[:size - 3]
        timestamp = int(timestamp)
        time_passed = str(datetime.timedelta(seconds= time - timestamp))
        size = len(str(transaction['timestamp']))
        amount = str(transaction['contractData']['amount'])
        amount = amount[:size - 9]
        amount = int(amount)
        price = requests.get('http://api.coinlayer.com/api/live?access_key=8939244a1f214d141489aa1b908d57ec')
        price = price.json()
        price =price['rates']['TRX']
        value = price * amount
        sender_address = transaction['contractData']['owner_address']
        reciever_address = transaction['contractData']['to_address']
        print(f'hash : {hash} \ntimestamp : {timestamp} \ntime passed : {time_passed} (HH:MM:SS) ago \nAmount : {amount} TRX \nPrice : {price} USD \nValue : {value} USD \nSender : {sender_address} \nReciever : {reciever_address} ')

tx = input('give tx hash : ')
check_transaction(tx)