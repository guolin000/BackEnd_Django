# import uuid
#
# random_uuid = uuid.uuid4()
# print(random_uuid)
# from user.models import SysRole
#
# if __name__ == '__main__':
#     roleList = SysRole.objects.raw("select role_id from sys_user_role where user_id=" + 1)
#     print(roleList)
import hashlib
from datetime import datetime

if __name__ == '__main__':
    # print(datetime.now().date())
    print(hashlib.md5("123456".encode()).hexdigest())
    # print(hashlib.md5(123456.encode()).hexdigest())
    # print("32323232.jpg"["32323232.jpg".rfind("."):])
