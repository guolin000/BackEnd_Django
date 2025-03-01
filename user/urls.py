from django.urls import path

from user.views import LoginView, TestView, CaptchaView, InfoView, SaveView, PwdView, ImageView, AvatarView, SearchView, \
    ActionView, CheckView, StatusView, PasswordView, GrantRole

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('info', InfoView.as_view(), name='info'),  # 查询用户信息
    path('save', SaveView.as_view(), name='save'),  # 添加或者修改用户信息
    path('uploadImage', ImageView.as_view(), name='uploadImage'),  # 头像上传
    path('updateAvatar', AvatarView.as_view(), name='updateAvatar'),  # 更新头像
    path('updateUserPwd', PwdView.as_view(), name='updateUserPwd'),  # 修改密码
    path('captcha', CaptchaView.as_view(), name='captcha'),  # 验证码
    path('search', SearchView.as_view(), name='search'),  # 用户信息查询
    path('action', ActionView.as_view(), name='action'),  # 用户信息操作
    path('check', CheckView.as_view(), name='check'),  # 用户名查重
    path('status', StatusView.as_view(), name='status'),  # 用户名查重
    path('grantRole', GrantRole.as_view(), name='grant'),  # 角色授权
    path('resetPassword', PasswordView.as_view(), name='resetPassword'),  # 重置密码
    path('test', TestView.as_view(), name='test'),  # 测试

]
