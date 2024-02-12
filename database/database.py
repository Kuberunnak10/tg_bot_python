import pickle


def save_to_db(user_id):

    with open('id_list.db', 'rb') as file:
        id_list = pickle.load(file)

    if user_id not in id_list:
        id_list.append(user_id)

    with open('id_list.db', 'wb') as file:
        pickle.dump(id_list, file)



