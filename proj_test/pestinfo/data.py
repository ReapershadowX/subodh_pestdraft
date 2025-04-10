from .models import pestinfo

pest1 = pestinfo(
    id= 1,
    name= 'Anthracnose', 
    short_description= 'Common mango fungal disease.', 
    full_description= 'Detailed info here...', 
    image_url= 'images/anthracnose.jpg')

pest_list = [pest1, ...]
