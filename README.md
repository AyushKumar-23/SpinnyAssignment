# SpinnyInternAssignment
# Name: Ayush Kumar
# Phone No.: 9873803727
# Email ID: kumarayush009@gmail.com

URL: 'https://spinnyassignment.onrender.com'<br>
------------------------------------------------------------<br><br>

<u>Credentials-</u>

1. username: admin <br>
password: admin<br>
Permission : All(Can login on the admin page)

2. username: staffUser <br>
password: spinny123<br>
Permission : All(Cannot login to admin page)

3. username: Testuser <br>
password: spinny123<br>
Permission: (NOT A STAFF MEMBER) shall be able to see boxes in the store<br>

Admin url : 'https://spinnyassignment.onrender.com/admin/'<br><br>

------------------------------------------------------------<br><br>

Variables Assigned -<br>
1.Average Area, A1 = 100 <br>
2.Average Volume, V1 = 100 <br>
3.Total Boxes added in a week, L1 = 100 <br>
4.Total Boxes added in a week by a user, L2=50 <br><br>

------------------------------------------------------------<br><br>
TASK 0: Building Models
1) I have used the Django's built in user model.
2) Box Model:
   The fields included in the box model are:
   creator, length, width ,height ,created_at ,updated_at

TASK 1: Add Api

url : 'https://spinnyassignment.onrender.com/add-box/'

Input fields: Length,width,height<br>
Permissions: User should be logged in and should be staff to add the box

TASK 2: Update Api

url : 'https://spinnyassignment.onrender.com/update-box/<int:pk>/'<br>
Sample url : 'https://spinnyassignment.onrender.com/update-box/38/'

Input fields: 
Length,width,height<br>
Permissions: 
Any Staff user should be able to update any box. but shall not be able to update the creator or creation date

TASK 3: List All Boxes

url : 'https://spinnyassignment.onrender.com/list-all-boxes/'

Permissions:
Any user shall be able to see boxes in the store. The "Created by" and the "Last Updated" field should be displayed only if the user is a staff member.

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
1) https://spinnyassignment.onrender.com/list-all-boxes/?length_more_than=1&created_by=admin
2) https://spinnyassignment.onrender.com/list-all-boxes/?area_more_than=5
3) https://spinnyassignment.onrender.com/list-all-boxes/?area_less_than=30&volume_more_than=1&created_by=admin
4) https://spinnyassignment.onrender.com/list-all-boxes/?created_after=2023-09-20

Sample Response:

{
        "length": 1.0,
        "width": 1.0,
        "height": 1.0,
        "area": 6.0,
        "volume": 1.0,
        "created_at": "2023-12-30T09:08:57.925343Z",
        "updated_at": "2023-12-30T09:08:57.942385Z"
}


TASK 4: List My Boxes

url: 'https://spinnyassignment.onrender.com/list-my-boxes/'

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
1) https://spinnyassignment.onrender.com/list-my-boxes/?width_less_than=100&volume_less_than=9
2) https://spinnyassignment.onrender.com/list-my-boxes/?length_more_than=100

Sample Response:

{
        "length": 1.0,
        "width": 1.0,
        "height": 1.0,
        "area": 6.0,
        "volume": 1.0,
        "created_at": "2023-12-30T09:08:57.925343Z",
        "updated_at": "2023-12-30T09:08:57.942385Z"
}


TASK 5: Delete Api

url: 'https://spinnyassignment.onrender.com/delete-box/<int:pk>/'<br>
Sample url : 'https://spinnyassignment.onrender.com/delete-box/38/'

Permissions:
Only the creater of the box shall be able to delete the box.<br><br>

------------------------------------------------------------<br><br>

CONDITIONS FULFILLED:
1. Average area of all added boxes should not exceed A1
2. Average volume of all boxes added by the current user shall not exceed V1
3. Total Boxes added in a week cannot be more than L1
4. Total Boxes added in a week by a user cannot be more than L2