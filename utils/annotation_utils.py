import json

def save_annotations(annotations, filename="dataset/annotations.json"):
    """保存标注数据"""
    with open(filename, "w") as f:
        json.dump(annotations, f, indent=4)
    return filename

def load_annotations(filename="dataset/annotations.json"):
    """加载标注数据"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
        