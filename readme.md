lincut

Install app:

```git clone https://github.com/prikhod/lincut.git```

 ```cd lincut```

```docker-compose up```

Example use:

``` curl -H "Content-Type: application/json"  -X POST -d 'http://mytestlink.td/a/a/s/s/' localhost:5000/make_link```

``` >>> {"result":"https://do.it/M"} ```

``` curl -H "Content-Type: application/json"  -X POST -d 'http://mytestlink.td/a/a/ccc'  localhost:5000/make_link```

``` >>> {"result":"https://do.it/N"} ```

etc...

``` curl -X GET  localhost:5000/get_links ```

```>>> {"result":{"https://do.it/C":"http://mytestlink.td/a/a/s/s/","https://do.it/D":"http://mytestlink.td/a/a/ccc"}} ```

```curl -X GET  localhost:5000/get_link/https://do.it/D```

```>>> {"result":"http://mytestlink.td/a/a/ccc"}```

```curl -X DELETE  localhost:5000/delete_link/https://do.it/D```

```{"result":1}```

``` curl -X GET  localhost:5000/get_links ```

```>>> {"result":{"https://do.it/C":"http://mytestlink.td/a/a/s/s/"}} ```


