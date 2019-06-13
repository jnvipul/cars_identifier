This file gives documentation for the cars 196 dataset.
(http://ai.stanford.edu/~jkrause/cars/car_dataset.html)

----------------------------------------
Metadata/Annotations
----------------------------------------
Descriptions of the files are as follows:

<b>-cars_meta.mat:</b>
  Contains a cell array of class names, one for each class.

<b>-cars_train_annos.mat:</b>
  Contains the variable 'annotations', which is a struct array of length
  num_images and where each element has the fields: <br>
    <b>bbox_x1</b>: Min x-value of the bounding box, in pixels<br>
    <b>bbox_x2</b>: Max x-value of the bounding box, in pixels<br>
    <b>bbox_y1</b>: Min y-value of the bounding box, in pixels<br>
    <b>bbox_y2</b>: Max y-value of the bounding box, in pixels<br>
    <b>class</b>: Integral id of the class the image belongs to. <br>
    <b>fname</b>: Filename of the image within the folder of images.<br>

<b>cars_test_annos.mat:</b><br>
  Same format as 'cars_train_annos.mat', except the class is not provided.

----------------------------------------
Submission file format
----------------------------------------
Files for submission should be .txt files with the class prediction for
image M on line M. Note that image M corresponds to the Mth annotation in
the provided annotation file. An example of a file in this format is
train_perfect_preds.txt

Included in the devkit are a script for evaluating training accuracy,
eval_train.m. Usage is:

(in MATLAB)
>> [accuracy, confusion_matrix] = eval_train('train_perfect_preds.txt')

If your training predictions work with this function then your testing
predictions should be good to go for the evaluation server, assuming
that they're in the same format as your training predictions.
