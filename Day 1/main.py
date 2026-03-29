import json

def read_json(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data
    
    
def write_json(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)




def clean_data(data):
    unique_users = set()
    cleaned_data = []
    new_rate={"one":1,"two":2,"three":3,"four":4,"five":5}
    for user in data:
        if(user.get("age")==None):
            user["age"] = "N/A"

        if(user["rating"] in new_rate):
            user["rating"] = float(new_rate[user["rating"]])
        
        if(user["name"]  in unique_users):
            unique_users.add(user["name"])
            cleaned_data.append(user)


        
    
    print(cleaned_data)

file_data = read_json("file.json")
clean_data(file_data)
write_json("file.json", file_data)
