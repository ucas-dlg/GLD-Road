import pickle
import cv2
import os

p_root = r"p_root"  # Replace with your p file path
img_root = r"img_root"  # Replace with your image file path
save_root = r"save_root"  # Replace with your save path



def read_p(p_path):
    with open(p_path, "rb") as f:
        data = pickle.load(f)
    return data


def vis_p(p_path, img_path, save_path):
    data = read_p(p_path)
    img = cv2.imread(img_path)
    for center, edges in data.items():
        for edge in edges:
            cv2.line(img, (list(center)[1], list(center)[0]), (list(edge)[1], list(edge)[0]), (0, 165, 255), 4)  # Note: exchange coordinates
    for (m, n) in data.keys():
        cv2.circle(img, (n, m), 4, (0, 255, 255), -1) # Note: exchange coordinates
    cv2.imwrite(save_path, img)


def main():
    names = os.listdir(p_root)
    for name in names:
        if not name.endswith(".p"):
            continue
        p_path = os.path.join(p_root, name)
        img_path = os.path.join(img_root, f"region_{name.replace('.p', '')}_sat.png")
        save_path = os.path.join(save_root, f"region_{name.replace('.p', '')}_sat.png")
        vis_p(p_path, img_path, save_path)


if __name__ == '__main__':
    main()
