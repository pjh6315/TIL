# PROJECT 05 DETAIL

### 1. Django Setting

* 프로젝트 생성 및 환경설정



### 2. base.html 구성

* boot strap css, js 추가

  * ```python
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
    
    ```

  * ```python
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
    
    ```

* navbar 구성

  * ```python
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav d-flex w-100">
          <li class="nav-item mr-auto">
            <a class="nav-link" href="{% url 'detail:qna' %}">Q&A<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'detail:mypage' %}">Mypage</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'detail:signup' %}">Signup</a>
          </li>
          
        </ul>
      </div>
    ```

* favicon

  * `    <link rel="shortcut icon" type='image/png' sizes='96*96' href="image link">`



### 3. 페이지 구성

* / (main page)

```html
{% extends 'base.html' %}




{% block container %}
<style>
    header{
        height: 350px;
        width: 100%;
        background-image: url("https://post-phinf.pstatic.net/MjAxNzA2MTlfMiAg/MDAxNDk3ODYwOTE2NDAw.MzMWKM07HtMjuSrCI1jEhwyzWtbLTM4TnGXLRlg5jRkg.Wv9HI_9F4seOMvJrMyqSpFWDKUEpA9j4wyhOEo3CP8Eg.JPEG/%EB%94%94%EC%A6%88%EB%8B%88_%EB%A7%8C%ED%99%94_%EC%86%8D_%EC%8B%A4%EC%A0%9C%EB%B0%B0%EA%B2%BD.jpg?type=w1200");   
        background-position: center center;
        background-size : cover;
        background-repeat: no-repeat;
    }
    
    footer{
    height: 50px;
    background-color: black;
    color: white;
    width: 100%;
    }
</style>


<header class='d-flex align-items-center justify-content-center'>
    
        <h1>Header</h1>
    
    
</header>

<footer class="px-5 d-flex justify-content-between align-items-center">
        <span>PJH</span>
        <a href="#">위로</a>
</footer>




{% endblock %}
```

* signup/

  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  <style>
      h1{
          text-align: center;
      }
      
    
  </style>
  <div class="container">
    <div class="row">
      <div class="col">
          <br>
          <br>
        <img src="https://i.ytimg.com/vi/XhmUL56gbRw/maxresdefault.jpg" width="350px" height="350px"></img>
      </div>
      <div class="col">
        <h1>Sign up</h1>
        <form>
    <div class="form-group">
      <label for="exampleInputEmail1">Email address</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    </div>
    <div class="form-group">
      <label for="exampleInputEmail1">Name</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Password</label>
      <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
    </div>
    <div class="form-group">
      <label for="exampleInputPassword1">Password Confirm</label>
      <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
        
      </div>
    </div>
  </div>
  
  
  
  {% endblock %}
  ```

  

* mypage

  ```html
  {% extends 'base.html' %}
  {% load static %}
  {% block container %}
  <style>
      .card{
          position: fixed;
      }
  </style>
  
  <div class="container">
    <div class="row">
      <div class="col-4">
          <div class="card" style="width: 18rem;">
    <img src="{% static '222.jpg' %}" class="card-img-top rounded-circle"  alt="...">
    <div class="card-body">
      <h5 class="card-title">Name</h5>
      <p class="card-text"><small class="text-muted">user@ssafy.com</small></p>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="card-link">Logout</a>
    </div>
  </div>
      </div>
      <div class="col-8">
          
    <img src="{% static '111.jpg' %}" class="card-img-top" alt="...">
   
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
  
  
      <img src="{% static '111.jpg' %}" class="card-img-top" alt="...">
   
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
  
  <img src="{% static '111.jpg' %}" class="card-img-top" alt="...">
   
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
  
  
  
      </div>
    </div>
  </div>
  
  
  {% endblock %}
  ```

  

* qna

```html
{% extends 'base.html' %}

{% block container %}
<style>
    h1{
        text-align:center;
    }
        
  
</style>
<h1>Q & A</h1>
<div class="container">
    <form class="row">

        <div class="form-group col-12 col-lg-6">
    <label for="exampleInputEmail1">제목</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
  </div>
  <div class="form-group col-12 col-lg-6">
    <label for="exampleInputEmail1">이메일</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
  </div>

  
  <div class="form-group col-12">
    <label for="exampleFormControlTextarea1">내용</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
  </div>
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>
    

{% endblock %}
```



* not_found

  * views.py

  * ```python
    def error(request,not_found):
        
        return render(request,'error.html',{'not_found':not_found})
    ```

  * urls.py

  * ```python
    path('<str:not_found>',views.error,name='error'),
    ```

  * error.html

  ```html
  {% extends 'base.html' %}
  
  {% block container %}
  <style>
      header{
          height: 350px;
          width: 100%;
          background-color: yellow;
      }
      
  </style>
  
  
  
  <header class='d-flex align-items-center justify-content-center'>
      
          <h1>{{ not_found }}</h1>
      
      
  </header>
  
  {% endblock %}
  ```

  

  