1. 다음은 부트스트랩의 어떤 component이며 아래와 같이 만들려면 어떤 class를 주어야하는가

> button component이고 .btn btn-danger class를 주어야한다



2. 다음은 부트스트랩의 어떤 component이며 아래와 동일하게 만들어 보시오.

> #alert-link

```python
<div class="alert alert-info" role="alert">
  A simple info alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
</div>
```



3. 다음 빈칸을 채우시오.

> " 부트스트랩 그리드 시스템은 레이아웃을 ( 12 ) 개의 column으로. ( 5 ) 개의 반응형 사이즈 조건을 사용하여 구축한다. "



4. 아래와 같은 분할을 grid system을 활용하여 만들어 보시오.

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <style>
        div {
            border: solid 1px black;
        }

        .row {
            background-color: moccasin;
        }
        
    </style>
    <title>Document</title>
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col">
                1 of 3
            </div>
            <div class="col-6">
                2 of 3 (wider)
            </div>
            <div class="col">
                3 of 3
            </div>
        </div>        
    </div>
</body>

</html>
```

