list = ['Makar Sidorov 24', 'Maria Kuznetsova 20', 'Reter Petrov 19', 'Ivan Ivanov 21']
print(sorted(list, key = lambda x: str(x[-2:])))
a = sorted(list, key = lambda x: str(x[-2:]))
print(a[0],[1])
