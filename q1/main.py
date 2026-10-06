import json 
import os
def analyze_log(filepath:str)->dict:
    result={'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath,'r',encoding='utf-8') as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                try:
                    data=json.loads(line)
                    result["total"]+=1
                    level=data.get("level")
                    user=data.get("user")
                    message=data.get("message")
                    if level is not None:
                        result["by_level"][level]=result["by_level"].get(level,0)+1
                    if user is not None:
                        result["by_user"][user]=result["by_user"].get(user,0)+1
                    if level=="ERROR":         
                        result["last_error"]=message
                except json.JSONDecodeError:
                    continue
                if isinstance(data,dict):
                    result["total"]+=1
                level=data.get("level","UNKNOWN")
                if level not in result["by_level"]:
                    result["by_level"][level]=0
                result["by_level"][level]+=1            
    except:
        return {}
    return result
