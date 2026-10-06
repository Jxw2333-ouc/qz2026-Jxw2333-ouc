import json
import os
#
class UserManager:
    def __init__(self):
        self.m_id=0
        self.users=[]
    def add_user(self,name:str,age:int)->dict:#返回用户字典
        self.m_id+=1 
        user = {"id": self.m_id, "name": name, "age": age}
        self.users.append(user)
        return user
    def get_user(self,user_id:int):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self,user_id:int, new_age:int):
        user = self.get_user(user_id)
        if user:
            user["age"] = new_age
            return True
        else:
            return False
    def remove_user(self,user_id:int):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        else:
            return False
    def list_users(self):
        return self.users
    def save_to_json(self, file_path:str):
        
    def load_from_json(self, file_path:str):