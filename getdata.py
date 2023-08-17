from roboflow import Roboflow
rf = Roboflow(api_key="hsFwAqeSXc2RzXx1BK5J")
project = rf.workspace("roboflow-gw7yv").project("fish-yzfml")
dataset = project.version(44).download("yolov8")
