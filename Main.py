import cv2
import json
import os
import time


def run(name, config):
    template_addr = config["template"]["address"] + config["template"]["name"]
    template = cv2.imread(template_addr)
    position_x = config["position"]["x"]
    position_y = config["position"]["y"]
    color_r = config["color"]["r"]
    color_b = config["color"]["g"]
    color_g = config["color"]["b"]
    size = config["font"]["size"]
    bold = config["font"]["bold"]
    face = cv2.FONT_HERSHEY_COMPLEX
    align = config["font"]["align"]
    if align == 4:
        textsize = cv2.getTextSize(name, face, size, bold)[0]
        position_x = int((template.shape[1] - textsize[0]) / 2)
    elif align == 3:
        textsize = cv2.getTextSize(name, face, size, bold)[0]
        position_x = int(template.shape[1] - textsize[0] - position_x)
    elif align == 2:
        textsize = cv2.getTextSize(name, face, size, bold)[0]
        position_x = int((template.shape[1] - textsize[0] - position_x)/2)
    cv2.putText(template, name, (position_x, position_y), face, size, (color_b, color_g, color_r),
                bold,
                cv2.LINE_AA)
    return template


def saver(name, template_addr, template):
    cv2.imwrite(name + template_addr[-4:], template)


def nameReader(config):
    with open("./namelist.txt", "r") as f:
        for line in f:
            saver(line.replace("\n", ""), config["template"]["name"], run(line.replace("\n", ""), config))


def configReader():
    with open("./config.json", "r") as f:
        config = json.load(f)
        nameReader(config)


def configGenerator():
    if not os.path.exists("./config.json"):
        with open("./config.json", "w") as f:
            f.write('{\n  "font": {\n\t"size" : 0.7,\n\t"bold" : 1,\n\t"align" : 1\n  },\n  "position" : {\n\t"x": 10,\n\t"y": 10\n  },'
                    '\n  "color" : {\n\t"r": 0,\n\t"g": 0,\n\t"b": 0\n  },\n  "template":{\n\t"address" : "",'
                    '\n\t"name": "template.png"\n  }\n}\n')
    with open("./config.json", "r") as f:
        config_tmp = json.load(f)
    config_tmp["font"]["size"] = float(input("font size (default:" + str(config_tmp["font"]["size"]) + ") : ") or \
                                       config_tmp["font"]["size"])
    config_tmp["font"]["bold"] = int(input("font thickness scale (default:" + str(config_tmp["font"]["bold"]) + ") : ") or \
                                     config_tmp["font"]["bold"])
    config_tmp["font"]["align"] = int(input("font align (default:" + str(config_tmp["font"]["align"]) + ") : ") or \
                                     config_tmp["font"]["align"])
    config_tmp["color"]["r"] = int(
        input("color R (default:" + str(config_tmp["color"]["r"]) + ") : ") or config_tmp["color"]["r"])
    config_tmp["color"]["g"] = int(
        input("color G (default:" + str(config_tmp["color"]["g"]) + ") : ") or config_tmp["color"]["g"])
    config_tmp["color"]["b"] = int(
        input("color B (default:" + str(config_tmp["color"]["b"]) + ") : ") or config_tmp["color"]["b"])
    config_tmp["template"]["address"] = input(
        "template addr (default:" + str(config_tmp["template"]["address"]) + ") : ") or \
                                        config_tmp["template"]["address"]
    config_tmp["template"]["name"] = input("template name (default:" + str(config_tmp["template"]["name"]) + ") : ") or \
                                     config_tmp["template"]["name"]
    config_tmp["position"]["x"], config_tmp["position"]["y"] = preview(run("test", config_tmp), config_tmp)
    with open("./config.json", "w") as f:
        f.write(json.dumps(config_tmp, indent=2))


def preview(template, config):
    speed = 1
    while config["font"]["align"] == 3:
        start = time.time()
        cv2.imshow('align_right', template)
        key = cv2.waitKey()
        if key == 0:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 1:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 2:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 3:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 61:
            config["font"]["size"] += 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 45:
            config["font"]["size"] -= 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 43:
            config["font"]["bold"] += 1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 95:
            if config["font"]["bold"] != 1:
                config["font"]["bold"] -= 1
            cv2.destroyAllWindows()
            template = run("test", config)

        else:
            return config["position"]['x'], config["position"]["y"]

    while config["font"]["align"] == 2:
        start = time.time()
        cv2.imshow('align_center', template)
        key = cv2.waitKey()
        if key == 0:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 1:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 2:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 3:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 61:
            config["font"]["size"] += 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 45:
            config["font"]["size"] -= 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 43:
            config["font"]["bold"] += 1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 95:
            if config["font"]["bold"] != 1:
                config["font"]["bold"] -= 1
            cv2.destroyAllWindows()
            template = run("test", config)

        else:
            return config["position"]['x'], config["position"]["y"]


    while config["font"]["align"] != 3 and config["font"]["align"] != 2:
        start = time.time()
        cv2.imshow('test', template)
        key = cv2.waitKey()
        if key == 0:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 1:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["y"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 2:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] -= speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 3:
            gap = time.time() - start
            if gap <= 0.1:
                speed += 1
            else:
                speed = 1
            config["position"]["x"] += speed
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 61:
            config["font"]["size"] += 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 45:
            config["font"]["size"] -= 0.1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 43:
            config["font"]["bold"] += 1
            cv2.destroyAllWindows()
            template = run("test", config)
        elif key == 95:
            if config["font"]["bold"] != 1:
                config["font"]["bold"] -= 1
            cv2.destroyAllWindows()
            template = run("test", config)

        else:
            return config["position"]['x'], config["position"]["y"]


if __name__ == '__main__':
    if input("1. Run with Settings\n2. Run Directly\nPlease select: ") or "1" == "1":
        configGenerator()
        configReader()
    else:
        configReader()

