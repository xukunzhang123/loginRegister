"""
前端界面设计与优化

在颜值即正义时代，没有css和js，样子真的令人无法接受。
然而，大多数使用Django的人都不具备很高的前端水平，通常也没有专业的前端工程师配合，自己写的css和js
却又惨不忍睹。可以使用开源前端css框架。Bootstrap4就是最好的css框架之一。
https://v4.bootcss.com/docs/getting-started/introduction/

（1）HTML：负责网页的架构；

（2）CSS：负责网页的样式，美化；

（3）JavaScript（JS）：负责网页的行为；

Bootstrap 核心汇总：
入门模板：https://v4.bootcss.com/docs/getting-started/introduction/
表单组件：https://v4.bootcss.com/docs/components/forms/
栅格系统：https://v4.bootcss.com/docs/layout/grid/ 最多将一行分为12列
警告框：https://v4.bootcss.com/docs/components/alerts/

index.html 中加入css模板
<!doctype html>
<html lang="zh-CN">
<head>
    <!-- 必须的 meta 标签 -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap 的 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
          integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>首页</title>
</head>
<body>
<h1>这是首页的模板界面</h1>

<!-- JavaScript 文件是可选的。从以下两种建议中选择一个即可！ -->

<!-- 选项 1：jQuery 和 Bootstrap 集成包（集成了 Popper） -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-7ymO4nGrkm372HoSbq1OY2DP4pEZnMiA+E0F3zPr+JQQtQ82gQ1HPY3QIVtztVua"
        crossorigin="anonymous"></script>

<!-- 选项 2：Popper 和 Bootstrap 的 JS 插件各自独立 -->
<!--
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-Lge2E2XotzMiwH69/MXB72yLpwyENMiOKX8zS8Qo7LDCvaBIWGL+GlRQEKIpYR04" crossorigin="anonymous"></script>
-->
</body>
</html>

login.html

<!doctype html>
<html lang="zh-CN">
<head>
    <!-- 必须的 meta 标签 -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap 的 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
          integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>首页</title>
</head>
<body>
<h1>这是首页的模板界面</h1>

<!-- JavaScript 文件是可选的。从以下两种建议中选择一个即可！ -->

<!-- 选项 1：jQuery 和 Bootstrap 集成包（集成了 Popper） -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-7ymO4nGrkm372HoSbq1OY2DP4pEZnMiA+E0F3zPr+JQQtQ82gQ1HPY3QIVtztVua"
        crossorigin="anonymous"></script>

<!-- 选项 2：Popper 和 Bootstrap 的 JS 插件各自独立 -->
<!--
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-Lge2E2XotzMiwH69/MXB72yLpwyENMiOKX8zS8Qo7LDCvaBIWGL+GlRQEKIpYR04" crossorigin="anonymous"></script>
-->
</body>
</html>

register.html

<!doctype html>
<html lang="zh-CN">
<head>
    <!-- 必须的 meta 标签 -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap 的 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
          integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>用户注册</title>
</head>
<body>
<!-- <div></div> 像是一个盒子（栅格），将表单进行封装显示。
<div style="width: 50%"> 占用宽度百分之50.建议找到栅格建议格式
-->
<div class="container">
    <div class="row">
        <div class="col-sm">
        </div>
        <div class="col-sm">
            <h3 style="text-align: center">用户注册</h3>
            <form>
                <div class="form-group">
                    <label>用户名</label>
                    <input type="text" class="form-control">
                </div>
                <div class="form-group">
                    <label>电子邮箱</label>
                    <input type="email" class="form-control">
                </div>
                <div class="form-group">
                    <label>密码</label>
                    <input type="password" class="form-control">
                    <small class="form-text text-muted">密码必须是字母、数字和特殊符号组成.</small>
                </div>
                <div class="form-group">
                    <label>确认密码</label>
                    <input type="password" class="form-control">
                    <small class="form-text text-muted">密码必须是字母、数字和特殊符号组成.</small>
                </div>
                <!-- float-right 将按钮飘到右侧 -->
                <!-- a 标签是添加链接，<ins>新用户注册</ins> 为标签添加下划线 class="text-success" 控制颜色success绿色，error红色-->
                <a href="/login/" class="text-success">
                    <ins>用户登录</ins>
                </a>
                <button type="submit" class="btn btn-primary float-right">注册</button>
            </form>
        </div>
        <div class="col-sm">
        </div>
    </div>
</div>
<!-- JavaScript 文件是可选的。从以下两种建议中选择一个即可！ -->

<!-- 选项 1：jQuery 和 Bootstrap 集成包（集成了 Popper） -->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-7ymO4nGrkm372HoSbq1OY2DP4pEZnMiA+E0F3zPr+JQQtQ82gQ1HPY3QIVtztVua"
        crossorigin="anonymous"></script>

<!-- 选项 2：Popper 和 Bootstrap 的 JS 插件各自独立 -->
<!--
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-Lge2E2XotzMiwH69/MXB72yLpwyENMiOKX8zS8Qo7LDCvaBIWGL+GlRQEKIpYR04" crossorigin="anonymous"></script>
-->
</body>
</html>
"""