import json
while True:
    with  open('data.json') as f:
        my_dict = json.load(f)

    print(my_dict)

    for key, value in my_dict.items():
        print(key, value)
        nytt_value = input(f'lägg till värde på {key}: ')
        if nytt_value == '':
            break
            value.append(nytt_value)

    with  open('data.json', 'w') as f:
        json.dump(my_dict,f)
