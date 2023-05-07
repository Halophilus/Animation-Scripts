import os
import random
import cv2

def random_loss(image, min_loss, max_loss):
    loss_factor = random.uniform(min_loss, max_loss)
    width = int(image.shape[1] * loss_factor)
    height = int(image.shape[0] * loss_factor)
    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(resized, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)

def process_images(input_folder_path, output_folder_path, min_loss, max_loss, transition_speed, loss_event_indices=None, random_loss_events=False):
    file_list = sorted(os.listdir(input_folder_path), key=lambda x: int(x.split('.')[0]))

    if random_loss_events:
        loss_event_index = random.randint(0, len(file_list) - 1)
        loss_event_indices = [loss_event_index]

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder_path, exist_ok=True)

    for i, file_name in enumerate(file_list):
        input_image_path = os.path.join(input_folder_path, file_name)
        output_image_path = os.path.join(output_folder_path, file_name)
        image = cv2.imread(input_image_path)

        if i in loss_event_indices:
            image = random_loss(image, min_loss, max_loss)
        elif any(i > loss_event_index for loss_event_index in loss_event_indices):
            nearest_event = min(filter(lambda x: i > x, loss_event_indices), key=lambda x: i - x)
            loss_transition = (i - nearest_event) / (transition_speed * (len(file_list) - nearest_event))
            transition_loss = max_loss - (max_loss - min_loss) * loss_transition
            image = random_loss(image, min_loss, transition_loss)

        cv2.imwrite(output_image_path, image, [cv2.IMWRITE_PNG_COMPRESSION, 9])


if __name__ == "__main__":
    input_folder_path = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LossEventMaker\\input"
    output_folder_path = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LossEventMaker\\output"
    min_loss = 0.4
    max_loss = 0.5
    transition_speed = 8

    random_loss_events= False

    if not random_loss_events:
        loss_event_indices = [1,101,223,344]
    else:
        loss_event_indices = None

    process_images(input_folder_path, output_folder_path, min_loss, max_loss, transition_speed, loss_event_indices, random_loss_events)
