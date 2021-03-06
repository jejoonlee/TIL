# ๐ Github

[Github ์ด๋?](#%EF%B8%8F-github์ด๋)

[How it works?](#%EF%B8%8F-how-it-works)

[.gitignore](#%EF%B8%8F-gitignore)



## โ๏ธ Github์ด๋?

> Git๊ณผ ๊ฐ์ version (์ปค๋ฐ)์ ๊ด๋ฆฌํ๋ค
>
> Github = Remote Repository (์๊ฒฉ ์ ์ฅ์)



## โ๏ธ How it works?

> Github๋ Remote (์๊ฒฉ) Repository (์ ์ฅ์)์ด๋ค
>
> ์ปค๋ฐ์ ๋ณด๋ด๊ณ  ๋ฐ์ ์ ์๋ค

![pushandpull](Github.assets/pushandpull.png)

1. ์ปค๋ฐ์ ์๊ฒฉ ์ ์ฅ์์ ๋ณด๋ด๋ ๊ฒ์ `PUSH`
2. ์ปค๋ฐ์ ์๊ฒฉ ์ ์ฅ์์์ ๋ฐ์ผ๋ฉด `PULL`



### ๐ ์๊ฒฉ ์ ์ฅ์ (Github)์ ์ปค๋ฐ์ PUSH ํ๋ ๋ฐฉ๋ฒ

> 1. ๋จผ์  ์๊ฒฉ ์ ์ฅ์๋ฅผ ๋ง๋ ๋ค (Github ๋ด์ new repository)
> 2. ๋ก์ปฌ ์ ์ฅ์์ version์ ์๊ฒฉ ์ ์ฅ์๋ก PUSH ํ๋ค

`https://github.com/jejoonlee/test.git`

์ด ์ฃผ์์ jejoonlee = Github์ username   /   test.git = ์ ์ฅ์ ์ด๋ฆ

```bash
$ git remote add origin https://github.com/jejoonlee/test.git
	# remote = ์๊ฒฉ์ ์ฅ์   /   add = ์ถ๊ฐํ๋ค   /   origin = origin์ผ๋ก
	# ๊น์ ์๊ฒฉ์ ์ฅ์์ origin์ผ๋ก ์ถ๊ฐ
	
$ git push <์๊ฒฉ์ ์ฅ์์ด๋ฆ> <๋ธ๋์น์ด๋ฆ>
	# ์๊ฒฉ์ ์ฅ์ ์ด๋ฆ = origin   /   ๋ธ๋์น์ด๋ฆ = master
	
$ git remote -v
	#์๊ฒฉ์ ์ฅ์ ํ์ธ
```

๐ `$ git remote add origin ....` ํ๋ฒ๋ง ์ธํํด ๋์ผ๋ฉด ๋จ

๐`$ git push origin master` ๋ฒ์ ์ด ์์ ๋ ๋๋ง๋ค ์๊ฒฉ์ ์ฅ์์ ๋ณด๋ด๊ณ  ์ถ์ผ๋ฉด, ์๋ ฅ์ ํด์ผ ํ๋ค

โ	๐จ๋ค ํ๊ธฐ ์ ์ ๊ผญ, `git init` , `git add .` , `git commit` ์ ํ  ๊ฒ 

โ	๐จ .git โ ๊ฐ๊ฐ ์๊ฒฉ ์ ์ฅ์๋ฅผ ๋ง๋ค์ด์ผ ํ๋ค



## โ๏ธ .gitignore

> ๋ฒ์ ์ด๋ ์๊ด์๋ ํ์ผ์ด ์์ ๋ ์ฌ์ฉ
>
> git์ด ์ถ์ ํ์ง ๋ชปํ๊ฒ ํ์ผ์ ๊ด๋ฆฌ

- .gitignore ํ์ผ์ ๋ง๋ ๋ค `$ touch .gitignore`
- ์์ฑ๋ ํ์ผ ์์ ๋ฒ์  ๊ด๋ฆฌ๊ฐ ํ์ ์๋ ํ์ผ/ํด๋ ์ด๋ฆ์ ๋ฃ์ผ๋ฉด ๋๋ค
- BUT, ์ด๋ฏธ ์ปค๋ฐ์ ํ๋ฉด ์์ ๋ ๊ฒ์ด track์ด ๋๋ค

[.gitignore](https://www.toptal.com/developers/gitignore/)



### .gitkeep

- ๋นํด๋๋ฅผ ๋ง๋ ๋ค (๊ด์ฉ์  used commonly)
- git์ ํจ์จ์ ์ผ๋ก ๊ด๋ฆฌํ๊ธฐ ์ํด ์ฐ์ด์ง๋ง, ๋นํด๋๋ ์๋ฏธ๊ฐ ์์

