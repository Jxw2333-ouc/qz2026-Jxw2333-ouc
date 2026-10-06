import json#跨程序
import os#路径
class UserManager:#面向对象编程
    def __init__(self):#主函数
        self.m_id=0
        self.users=[]
    def add_user(self,name,age)->dict:#返回数据是字典类型
        self.m_id+=1 
        user = {"id": self.m_id, "name": name, "age": age}
        self.users.append(user)
        return user
    def get_user(self,user_id):#获取用户信息
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self,user_id, new_age):#更新年龄数据
        user = self.get_user(user_id)
        if user:
            user["age"] = new_age
            return True
        else:
            return False
    def remove_user(self,user_id):#删除用户
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        else:
            return False
    def list_users(self):#列出所有用户
        return self.users
    def save_to_json(self,file_path):#保存用户数据到JSON文件
        with open(file_path, 'w',encoding='utf-8') as f:
            json.dump(self.users, f)
    def load_from_json(self,file_path):#下载用户数据从JSON文件
        if os.path.exists(file_path):
            with open(file_path, 'r',encoding='utf-8') as f:
                self.users = json.load(f)
                if self.users:
                    self.m_id = max(user["id"] for user in self.users)