# SpinnyAssignment
# Name: Ayush Kumar
# Phone No.: 9873803727
# Email ID: kumarayush009@gmail.com


Average Area, A1 = 100
Average Volume, V1 = 100
Total Boxes added in a week, L1 = 100
Total Boxes added in a week by a user, L2=50


TASK 0: Building Models
1) I have used the Django's built in user model.
2) Box Model:
   The fields included in the box model are:
   creator, length, width ,height ,created_at ,updated_at

TASK 1: Add Api

url : '/add-box/'

Input fields: Length,width,height
Permissions: User should be logged in and should be staff to add the box

TASK 2: Update Api

url : '/update-box/<int:pk>/'

Input fields: 
Length,width,height
Permissions: 
Any Staff user should be able to update any box. but shall not be able to update the creator or creation date

TASK 3: List All Boxes

url : '/list-all-boxes/'

Response:
        1. Length
        2. width
        3. Height
        4. Area
        5. Volume
        6. Created By
        7. Last Updated

Permissions:
Any user shall be able to see boxes in the store. The "Createg by" and the "Last Updated" field should be displayed only if the user is a staff member.

Filters:
1. length_more_than
2. length_less_than
3. width_more_than
4. width_less_than
5. height_more_than
6. height_less_than
7. area_more_than
8. area_less_than
9. volume_more_than
10.volume_less_than
11.created_by
12.created_before
13.created_after

Example URL for applying filters: 
1) http://127.0.0.1:8000/list-all-boxes/?length_more_than=1&created_by=admin
2) http://127.0.0.1:8000/list-all-boxes/?area_more_than=20
3) http://127.0.0.1:8000/list-all-boxes/?area_less_than=30&volume_more_than=5&created_by=admin


TASK 4: List My Boxes

url: '/list-my-boxes/'

Response:
        1. Length
        2. width
        3. Height
        4. Area
        5. Volume
        6. Created By
        7. Last Updated

Permissions:
Only Staff user shall be able to see his/her created boxes in the store.

Filters:
1. length_more_than
2. length_less_than
3. width_more_than
4. width_less_than
5. height_more_than
6. height_less_than
7. area_more_than
8. area_less_than
9. volume_more_than
10.volume_less_than

Example URL for applying filters: 
1) http://127.0.0.1:8000/list-my-boxes/?width_less_than=100&volume_less_than=9
2) http://127.0.0.1:8000/list-my-boxes/?length_more_than=100


TASK 5: Delete Api

url: "/delete-box/<int:pk>/"

Permissions:
Only the creater of the box shall be able to delete the box.



CONDITIONS FULFILLED:
1. Average area of all added boxes should not exceed A1
2. Average volume of all boxes added by the current user shall not exceed V1
3. Total Boxes added in a week cannot be more than L1
4. Total Boxes added in a week by a user cannot be more than L2