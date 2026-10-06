import json
import os
class UserManager:
    def __init__(self):

    def add_user(self,name:str,age:int):

    def get_user(self,user_id:int):

    def update_age(self,user_id:int, new_age:int):

    def remove_user(self,user_id:int):

    def list_users(self):

    def save_to_json(self, file_path:str):

    def load_from_json(self, file_path:str):        